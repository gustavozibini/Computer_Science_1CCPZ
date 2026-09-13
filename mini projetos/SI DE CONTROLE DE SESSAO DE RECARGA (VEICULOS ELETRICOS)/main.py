"""
SISTEMA INTELIGENTE DE CONTROLE DE SESSAO DE RECARGA (VEICULOS ELETRICOS)
Inspirado no conceito GoodWe Smart Energy Controller
Disciplina: Arquitetura de Computadores - Raspberry Pi Pico (RP2040)
"""

import time
import struct
from machine import Pin, SPI, I2C
import framebuf

# ==============================================================================
# 1. MAPEAMENTO DE HARDWARE E PINAGEM (RP2040)
# ==============================================================================

# Dispositivos de Saida Digital Simples (LEDs Fisicos)
led_verde = Pin(1, Pin.OUT)  # GP1 -> Recarga Autorizada
led_amarelo = Pin(5, Pin.OUT)  # GP5 -> Recarga Reduzida
led_vermelho = Pin(9, Pin.OUT)  # GP9 -> Recarga Bloqueada

# Barramento SPI0 - Display ILI9341 (Saida Grafica)
spi_sck = Pin(18)  # GP18: SPI0 Clock
spi_mosi = Pin(19)  # GP19: SPI0 TX / MOSI
spi_miso = Pin(16)  # GP16: SPI0 RX / MISO
tft_cs = Pin(17, Pin.OUT, value=1)  # GP17: Chip Select
tft_dc = Pin(15, Pin.OUT, value=0)  # GP15: Data / Command
tft_rst = Pin(14, Pin.OUT, value=1)  # GP14: Reset

spi = SPI(0, baudrate=30_000_000, polarity=0, phase=0,
          sck=spi_sck, mosi=spi_mosi, miso=spi_miso)

# Barramento I2C0 - Touch Capacitivo FT6206 (Entrada do Usuario)
touch_sda = Pin(20)  # GP20: I2C0 SDA
touch_scl = Pin(21)  # GP21: I2C0 SCL
i2c = I2C(0, sda=touch_sda, scl=touch_scl, freq=400_000)


# ==============================================================================
# 2. DEFINICAO DE CORES RGB565 E DRIVERS
# ==============================================================================

def color565(r, g, b):
    return ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)


BLACK = color565(0, 0, 0)
WHITE = color565(255, 255, 255)
GREEN = color565(0, 235, 120)
DARK_GREEN = color565(10, 65, 25)
YELLOW = color565(255, 215, 0)
DARK_YELLOW = color565(75, 65, 10)
RED = color565(255, 75, 75)
DARK_RED = color565(80, 15, 15)
BLUE = color565(30, 144, 255)
DARK_BLUE = color565(10, 25, 60)
GRAY = color565(130, 140, 150)
DARK_GRAY = color565(40, 45, 55)

BG_COLOR = color565(15, 18, 25)
CARD_BG = color565(24, 30, 42)
CARD_BORDER = color565(45, 55, 72)


class DisplayILI9341:
    def __init__(self, spi, cs, dc, rst, width=240, height=320):
        self.spi = spi
        self.cs = cs
        self.dc = dc
        self.rst = rst
        self.width = width
        self.height = height
        self.init_display()

    def write_cmd(self, cmd):
        self.dc.low()
        self.cs.low()
        self.spi.write(bytearray([cmd]))
        self.cs.high()

    def write_data(self, data):
        self.dc.high()
        self.cs.low()
        self.spi.write(data)
        self.cs.high()

    def init_display(self):
        self.rst.high()
        time.sleep_ms(10)
        self.rst.low()
        time.sleep_ms(20)
        self.rst.high()
        time.sleep_ms(150)

        self.write_cmd(0x01)  # Software Reset
        time.sleep_ms(120)
        self.write_cmd(0x28)  # Display OFF

        # Configuracao de Memoria e Varredura (Orientacao Retrato)
        self.write_cmd(0x36)
        self.write_data(bytearray([0x48]))

        # Formato de Pixel: 16-bit RGB565
        self.write_cmd(0x3A)
        self.write_data(bytearray([0x55]))

        self.write_cmd(0x11)  # Sleep Out
        time.sleep_ms(120)
        self.write_cmd(0x29)  # Display ON

    def set_window(self, x0, y0, x1, y1):
        x0 = max(0, min(self.width - 1, x0))
        x1 = max(0, min(self.width - 1, x1))
        y0 = max(0, min(self.height - 1, y0))
        y1 = max(0, min(self.height - 1, y1))
        self.write_cmd(0x2A)  # Column Address Set
        self.write_data(struct.pack(">HH", x0, x1))
        self.write_cmd(0x2B)  # Page Address Set
        self.write_data(struct.pack(">HH", y0, y1))
        self.write_cmd(0x2C)  # Memory Write

    def fill(self, color):
        self.fill_rect(0, 0, self.width, self.height, color)

    def fill_rect(self, x, y, w, h, color):
        if x >= self.width or y >= self.height or w <= 0 or h <= 0:
            return
        w = min(w, self.width - x)
        h = min(h, self.height - y)
        self.set_window(x, y, x + w - 1, y + h - 1)
        pixel = struct.pack(">H", color)
        chunk = pixel * min(w * h, 512)
        total = w * h
        self.dc.high()
        self.cs.low()
        while total > 0:
            count = min(total, 512)
            self.spi.write(chunk[:count * 2])
            total -= count
        self.cs.high()

    def rect(self, x, y, w, h, color, thickness=1):
        for i in range(thickness):
            self.fill_rect(x + i, y + i, w - 2 * i, 1, color)
            self.fill_rect(x + i, y + h - 1 - i, w - 2 * i, 1, color)
            self.fill_rect(x + i, y + i, 1, h - 2 * i, color)
            self.fill_rect(x + w - 1 - i, y + i, 1, h - 2 * i, color)

    def blit(self, buf, x, y, w, h):
        self.set_window(x, y, x + w - 1, y + h - 1)
        self.dc.high()
        self.cs.low()
        self.spi.write(buf)
        self.cs.high()

    def text(self, s, x, y, color=WHITE, bg_color=CARD_BG, scale=1):
        if x >= self.width or y >= self.height:
            return
        max_chars = (self.width - x) // (8 * scale)
        if max_chars <= 0:
            return
        s = s[:max_chars]
        base_w = len(s) * 8
        if base_w <= 0:
            return

        # Correcao de Endianness para casar perfeitamente a cor de fundo do texto
        def swap16(c):
            return ((c & 0xFF) << 8) | ((c >> 8) & 0xFF)

        buf = bytearray(base_w * 8 * 2)
        fb = framebuf.FrameBuffer(buf, base_w, 8, framebuf.RGB565)
        fb.fill(swap16(bg_color))
        fb.text(s, 0, 0, swap16(color))
        self.blit(buf, x, y, base_w, 8)

    def draw_circle(self, cx, cy, r, color, fill=True):
        if fill:
            for y in range(-r, r + 1):
                x_span = int((r * r - y * y) ** 0.5)
                self.fill_rect(cx - x_span, cy + y, 2 * x_span + 1, 1, color)
        else:
            x = r
            y = 0
            err = 0
            while x >= y:
                for px, py in [(cx + x, cy + y), (cx + y, cy + x), (cx - y, cy + x), (cx - x, cy + y),
                               (cx - x, cy - y), (cx - y, cy - x), (cx + y, cy - x), (cx + x, cy - y)]:
                    if 0 <= px < self.width and 0 <= py < self.height:
                        self.fill_rect(px, py, 1, 1, color)
                y += 1
                err += 1 + 2 * y
                if 2 * (err - x) + 1 > 0:
                    x -= 1
                    err += 1 - 2 * x


class TouchFT6206:
    def __init__(self, i2c, addr=0x38):
        self.i2c = i2c
        self.addr = addr

    def get_point(self):
        try:
            self.i2c.writeto(self.addr, b'\x00')
            data = self.i2c.readfrom(self.addr, 16)
            touches = data[2]
            if touches in (1, 2):
                raw_x = ((data[3] & 0x0F) << 8) | data[4]
                raw_y = ((data[5] & 0x0F) << 8) | data[6]

                # Mapeamento com inversao de eixos para o display ILI9341
                x = 240 - raw_x
                y = 320 - raw_y
                x = max(0, min(239, x))
                y = max(0, min(319, y))
                return x, y
        except Exception:
            pass
        return None


# ==============================================================================
# 3. INTERFACE GRAFICA E LOGICA DE CONTROLE
# ==============================================================================

display = DisplayILI9341(spi, tft_cs, tft_dc, tft_rst)
touch = TouchFT6206(i2c)

# Estado inicial do sistema (Cenario 1)
geracao = 4000  # Watts
consumo = 1500  # Watts


def desenhar_layout_estatico():
    display.fill(BG_COLOR)

    # Top Header
    display.fill_rect(0, 0, 240, 30, CARD_BG)
    display.rect(0, 0, 240, 30, CARD_BORDER)
    display.text("SMART ENERGY CONTROLLER", 28, 6, WHITE, CARD_BG)
    display.text("Recarga VE / Arq RP2040", 28, 18, GRAY, CARD_BG)

    # Painel de Bases Numericas (Fixo)
    display.fill_rect(8, 176, 224, 56, CARD_BG)
    display.rect(8, 176, 224, 56, CARD_BORDER)
    display.text("BASES NUMERICAS (E/S)", 36, 182, WHITE, CARD_BG)

    # Botoes de Toque (Cenarios da Disciplina)
    # Cenario 1 (Verde)
    display.fill_rect(8, 238, 70, 34, DARK_GREEN)
    display.rect(8, 238, 70, 34, GREEN)
    display.text("CEN 1", 26, 244, WHITE, DARK_GREEN)
    display.text("4000W", 22, 256, GREEN, DARK_GREEN)

    # Cenario 2 (Amarelo)
    display.fill_rect(85, 238, 70, 34, DARK_YELLOW)
    display.rect(85, 238, 70, 34, YELLOW)
    display.text("CEN 2", 103, 244, WHITE, DARK_YELLOW)
    display.text("1800W", 99, 256, YELLOW, DARK_YELLOW)

    # Cenario 3 (Vermelho)
    display.fill_rect(162, 238, 70, 34, DARK_RED)
    display.rect(162, 238, 70, 34, RED)
    display.text("CEN 3", 180, 244, WHITE, DARK_RED)
    display.text("1000W", 176, 256, RED, DARK_RED)

    # Botoes de Ajuste de Energia (+500W / -500W)
    # Botao Esquerda: Energia / +500
    display.fill_rect(8, 276, 108, 38, CARD_BG)
    display.rect(8, 276, 108, 38, BLUE)
    display.text("Energia", 34, 281, WHITE, CARD_BG)
    display.text("+500", 46, 296, GREEN, CARD_BG)

    # Botao Direita: Energia / -500
    display.fill_rect(124, 276, 108, 38, CARD_BG)
    display.rect(124, 276, 108, 38, BLUE)
    display.text("Energia", 150, 281, WHITE, CARD_BG)
    display.text("-500", 162, 296, RED, CARD_BG)


def atualizar_interface(ger, cons, disp):
    # Determina o estado operacional e aciona as saidas (LEDs fisicos e virtuais)
    if disp >= 1000:
        status_txt = "RECARGA AUTORIZADA"
        st_bg = DARK_GREEN
        st_border = GREEN
        st_color = GREEN
        led_verde.high()
        led_amarelo.low()
        led_vermelho.low()
        active_led = 'verde'
    elif disp > 0:
        status_txt = " RECARGA REDUZIDA "
        st_bg = DARK_YELLOW
        st_border = YELLOW
        st_color = YELLOW
        led_verde.low()
        led_amarelo.high()
        led_vermelho.low()
        active_led = 'amarelo'
    else:
        status_txt = " RECARGA BLOQUEADA"
        st_bg = DARK_RED
        st_border = RED
        st_color = RED
        led_verde.low()
        led_amarelo.low()
        led_vermelho.high()
        active_led = 'vermelho'

    # 1. Card de Status e LEDs Virtuais
    display.fill_rect(8, 34, 224, 58, st_bg)
    display.rect(8, 34, 224, 58, st_border, thickness=2)
    display.text(status_txt, 48, 42, WHITE, st_bg)

    # LEDs Virtuais sincronizados com os LEDs fisicos (Verde -> Amarelo -> Vermelho)
    # Verde (Esquerda: x=60, y=70)
    display.draw_circle(60, 70, 9, GREEN if active_led == 'verde' else DARK_GRAY, fill=True)
    display.draw_circle(60, 70, 9, GREEN, fill=False)

    # Amarelo (Centro: x=120, y=70)
    display.draw_circle(120, 70, 9, YELLOW if active_led == 'amarelo' else DARK_GRAY, fill=True)
    display.draw_circle(120, 70, 9, YELLOW, fill=False)

    # Vermelho (Direita: x=180, y=70)
    display.draw_circle(180, 70, 9, RED if active_led == 'vermelho' else DARK_GRAY, fill=True)
    display.draw_circle(180, 70, 9, RED, fill=False)

    # 2. Metricas de Potencia
    # Geracao
    display.fill_rect(8, 96, 108, 36, CARD_BG)
    display.rect(8, 96, 108, 36, CARD_BORDER)
    display.text("GERACAO", 34, 101, WHITE, CARD_BG)
    display.text(f"{ger:>4} W", 34, 115, GREEN, CARD_BG)

    # Consumo
    display.fill_rect(124, 96, 108, 36, CARD_BG)
    display.rect(124, 96, 108, 36, CARD_BORDER)
    display.text("CONSUMO", 150, 101, WHITE, CARD_BG)
    display.text(f"{cons:>4} W", 150, 115, RED, CARD_BG)

    # Energia Disponivel
    display.fill_rect(8, 136, 224, 36, CARD_BG)
    display.rect(8, 136, 224, 36, CARD_BORDER)
    display.text("Energia Disponivel", 48, 141, WHITE, CARD_BG)
    display.text(f"{disp:>5} W", 90, 155, st_color, CARD_BG)

    # 3. Bases Numericas (Conceito de Arquitetura de Computadores)
    val_16 = disp & 0xFFFF
    bin_str = f"{val_16:016b}"
    bin_fmt = f"{bin_str[0:4]} {bin_str[4:8]} {bin_str[8:12]} {bin_str[12:16]}"
    hex_fmt = f"0x{val_16:04X}"

    display.fill_rect(12, 196, 216, 32, CARD_BG)
    # Linha 1: DEC e HEX (Rotulos e unidade W em Branco; Resultados na cor correspondente st_color)
    display.text("DEC:", 16, 198, WHITE, CARD_BG)
    display.text(f"{disp:>5}", 50, 198, st_color, CARD_BG)
    display.text("W", 93, 198, WHITE, CARD_BG)

    display.text("HEX:", 118, 198, WHITE, CARD_BG)
    display.text(f"{hex_fmt}", 154, 198, st_color, CARD_BG)

    # Linha 2: BIN (Rotulo em Branco; Resultado de 16 bits na cor correspondente st_color)
    display.text("BIN:", 16, 212, WHITE, CARD_BG)
    display.text(f"{bin_fmt}", 56, 212, st_color, CARD_BG)

    # 4. Envio de dados formatados ao Terminal Serial
    print("=" * 60)
    print("SISTEMA INTELIGENTE DE RECARGA (VE) - RP2040")
    print(f"GERACAO:    {ger:>5} W")
    print(f"CONSUMO:    {cons:>5} W")
    print(f"DISPONIVEL: {disp:>5} W")
    print(f"ESTADO:     {status_txt.strip()}")
    print("-" * 60)
    print("CONVERSAO DE BASES NUMERICAS (Potencia Disponivel):")
    print(f"  Decimal:     {disp:>6} W")
    print(f"  Binario:     {bin_fmt}")
    print(f"  Hexadecimal: {hex_fmt}")
    print("=" * 60)
    print()


# ==============================================================================
# 4. EXECUCAO PRINCIPAL (LOOP DE ENTRADA, PROCESSAMENTO E SAIDA)
# ==============================================================================

desenhar_layout_estatico()
disponivel = geracao - consumo
atualizar_interface(geracao, consumo, disponivel)

last_touch_time = 0
touch_cooldown_ms = 350

print("Sistema Inicializado com Sucesso no Raspberry Pi Pico!")
print("Toque nos botoes na tela para alternar cenarios ou ajustar a potencia.")

while True:
    agora = time.ticks_ms()
    pt = touch.get_point()

    if pt and time.ticks_diff(agora, last_touch_time) > touch_cooldown_ms:
        last_touch_time = agora
        tx, ty = pt
        print(f"[Touch] Toque detectado em X={tx}, Y={ty}")

        mudou = False

        # Verifica toque em Cenario 1 (x: 8..78, y: 238..272)
        if 8 <= tx <= 78 and 238 <= ty <= 272:
            geracao = 4000
            consumo = 1500
            mudou = True

        # Verifica toque em Cenario 2 (x: 85..155, y: 238..272)
        elif 85 <= tx <= 155 and 238 <= ty <= 272:
            geracao = 1800
            consumo = 1500
            mudou = True

        # Verifica toque em Cenario 3 (x: 162..232, y: 238..272)
        elif 162 <= tx <= 232 and 238 <= ty <= 272:
            geracao = 1000
            consumo = 1800
            mudou = True

        # Verifica toque em [+500W] (Esquerda: x: 8..116, y: 276..316)
        elif 8 <= tx <= 116 and 276 <= ty <= 316:
            geracao = min(6000, geracao + 500)
            mudou = True

        # Verifica toque em [-500W] (Direita: x: 124..232, y: 276..316)
        elif 124 <= tx <= 232 and 276 <= ty <= 316:
            geracao = max(0, geracao - 500)
            mudou = True

        if mudou:
            disponivel = geracao - consumo
            atualizar_interface(geracao, consumo, disponivel)

    time.sleep_ms(20)