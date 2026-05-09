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


nomes = ["ana", "leo", "bia", "juca"]
for i in range(len(nomes) - 1):
    for j in range(i + 1, len(nomes)):
        print(nomes[i], nomes[j])

