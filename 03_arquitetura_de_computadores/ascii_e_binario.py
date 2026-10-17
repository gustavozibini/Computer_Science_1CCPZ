"""
Como o computador guarda texto: cada letra vira um número (código ASCII),
e cada número vira 8 bits (1 byte).

Mostra, para cada letra: letra -> código ASCII -> binário de 8 bits.
No final, conta quantos caracteres, bytes e bits tem a mensagem.
"""

# ord() devolve o código ASCII de um caractere (aqui, o espaço = 32)
letra = " "

codigo = ord(letra)

print("letra:", letra)
print("codigo ASCII:", codigo)
# {:08b} formata o número em binário, com 8 dígitos (completa com zeros à esquerda)
print("binario:", "{:08b}".format(codigo,))

# Exemplo com um texto fixo
texto = "oioe"

for letra in texto:
    codigo = ord(letra)

    print(
        letra,
        "->",
        codigo,
        "->",
        "{:08b}".format(codigo)
    )



# Mesmo exemplo, agora com a mensagem digitada pelo usuário
texto = input("digite a msg:")

for letra in texto:
    codigo = ord(letra)

    print(
        letra,
        "->",
        codigo,
        "->",
        "{:08b}".format(codigo)
    )

print()
qtd_bytes = len(texto)   # 1 caractere ASCII = 1 byte
print("caracteres:", qtd_bytes)
print("bytes", qtd_bytes)
print("bits:", qtd_bytes * 8)   # 1 byte = 8 bits
