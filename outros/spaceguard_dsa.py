"""SpaceGuard - monitoramento simples de missao espacial."""

from typing import Optional


historico_leituras = []
leitura_atual: Optional[dict] = None


def analisar_leitura(leitura):
    alertas = []

    if leitura["temperatura"] < 10:
        alertas.append("Alerta de temperatura muito baixa")
    if leitura["temperatura"] > 80:
        alertas.append("Alerta de superaquecimento")
    if leitura["energia"] < 20:
        alertas.append("Economia de energia")
    if leitura["comunicacao"] == 0:
        alertas.append("Falha de comunicacao")
    if leitura["status_operacional"] == 0:
        alertas.append("Falha operacional detectada")

    if not alertas:
        alertas.append("Status normal da missao")

    return alertas


def ler_numero(mensagem, minimo=None, maximo=None):
    while True:
        try:
            valor = float(input(mensagem).strip())
            if minimo is not None and valor < minimo:
                print(f"Valor invalido. Digite um numero maior ou igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Valor invalido. Digite um numero menor ou igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Entrada invalida. Digite um numero.")


def ler_binario(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor in {"0", "1"}:
            return int(valor)
        print("Entrada invalida. Digite apenas 0 ou 1.")


def inserir_dados():
    global leitura_atual

    print("\n--- Insercao de Dados da Missao ---")
    temperatura = ler_numero("Temperatura da nave: ")
    energia = ler_numero("Nivel de energia (%): ", 0, 100)
    comunicacao = ler_binario("Status da comunicacao (1 = OK, 0 = Falha): ")
    status_operacional = ler_binario("Status operacional (1 = OK, 0 = Falha): ")

    leitura_atual = {
        "temperatura": temperatura,
        "energia": energia,
        "comunicacao": comunicacao,
        "status_operacional": status_operacional,
    }

    historico_leituras.append(leitura_atual.copy())
    print("Leitura registrada com sucesso.")


def visualizar_status():
    if leitura_atual is None:
        print("\nNenhuma leitura registrada ate o momento.")
        return

    atual = leitura_atual

    print("\n--- Status Atual da Missao ---")
    print(f"Temperatura: {atual['temperatura']:.1f} C")
    print(f"Energia: {atual['energia']:.1f}%")
    print(f"Comunicacao: {'OK' if atual['comunicacao'] == 1 else 'Falha'}")
    situacao = "OK" if atual["status_operacional"] == 1 else "Falha"
    print(f"Status operacional: {situacao}")


def executar_analise():
    if leitura_atual is None:
        print("\nNenhuma leitura registrada para analise.")
        return

    atual = leitura_atual

    print("\n--- Analise Automatica ---")
    for alerta in analisar_leitura(atual):
        print(f"- {alerta}")


def visualizar_historico():
    if not historico_leituras:
        print("\nHistorico vazio.")
        return

    print("\n--- Historico de Leituras ---")
    for indice, leitura in enumerate(historico_leituras, start=1):
        comunicacao = "OK" if leitura["comunicacao"] == 1 else "Falha"
        operacional = "OK" if leitura["status_operacional"] == 1 else "Falha"
        print(
            f"{indice}. Temperatura: {leitura['temperatura']:.1f} C | "
            f"Energia: {leitura['energia']:.1f}% | "
            f"Comunicacao: {comunicacao} | "
            f"Status operacional: {operacional}"
        )


def exibir_menu():
    print("\n=== SpaceGuard ===")
    print("1. Inserir dados da missao")
    print("2. Visualizar status atual")
    print("3. Executar analise automatica")
    print("4. Visualizar historico de leituras")
    print("5. Encerrar sistema")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            inserir_dados()
        elif opcao == "2":
            visualizar_status()
        elif opcao == "3":
            executar_analise()
        elif opcao == "4":
            visualizar_historico()
        elif opcao == "5":
            print("\nEncerrando o sistema SpaceGuard.")
            break
        else:
            print("\nOpcao invalida. Tente novamente.")


if __name__ == "__main__":
    main()
