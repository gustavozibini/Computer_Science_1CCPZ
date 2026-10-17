"""
Aula - Listas e strings.

O começo (comentado) mostra o básico: acessar itens por índice, append, len e for.
Dica: o índice começa em 0 e o -1 pega sempre o último item.
O código ativo, no final, mostra todos os pares de nomes diferentes.
"""

# lista_frutas = [ "banana", "morango", "limao"]
# print(lista_frutas[1])
#
# lista_frutas.append("uva")
# print(lista_frutas[-1])  # -1 sempre acessa o ultimo elemento
#
#
# tamanho = len(lista_frutas)
# print(tamanho)
#
# for i in range(tamanho):
#     print(lista_frutas[i])
#
# print()
#
# for fruta in lista_frutas:
#     print(fruta)
#
# msg = "oi fulano"
# print(msg[0])
#
#
# for i in range(len(msg)):
#     print(msg[i])


# Gera todos os pares possíveis (ana-leo, ana-bia, ...) sem repetir:
# o j sempre começa depois do i
nomes = ["ana", "leo", "bia", "juca"]
for i in range(len(nomes) - 1):
    for j in range(i + 1, len(nomes)):
        print(nomes[i], nomes[j])

