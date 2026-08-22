letra = " "

codigo = ord(letra)

print("letra:", letra)
print("codigo ASCII:", codigo)
print("binario:", "{:08b}".format(codigo,))

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
qtd_bytes = len(texto)
print("caracteres:", qtd_bytes)
print("bytes", qtd_bytes)
print("bits:", qtd_bytes * 8)