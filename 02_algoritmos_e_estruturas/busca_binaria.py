"""
Busca binária: acha um valor numa lista JÁ ORDENADA muito mais rápido que a busca linear.

Ideia: olhar o item do meio.
  - Se for o valor procurado, achou.
  - Se o meio for menor, o valor está na metade da direita.
  - Se o meio for maior, está na metade da esquerda.
Assim, a cada passo descartamos metade da lista.
"""

# Versão antiga (procurando o 10), guardada como anotação:
# def busca_binaria(lista, valor):
#     inicio = 0
#     fim = len(lista) -1
#
#     while inicio <= fim:
#         meio = (inicio + fim) // 2
#         if lista[meio] == valor:
#             return meio
#         elif lista[meio] < valor:
#             inicio = meio + 1
#         else:
#             fim = meio - 1
#     return -1
#
# numeros = [3,7,10,15,21,28,32,40,47,51,63]
# posicao = busca_binaria(numeros, 10)
# print(posicao)

def busca_binaria(lista, valor):
    """Devolve a posição do valor na lista, ou -1 se ele não existir."""
    inicio = 0
    fim = len(lista) -1

    while inicio <= fim:
        meio = (inicio + fim) // 2   # // é divisão inteira (sem casas decimais)
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            inicio = meio + 1        # descarta a metade da esquerda
        else:
            fim = meio - 1           # descarta a metade da direita
    return -1

numeros = [3,7,10,15,21,28,32,40,47,51,63]   # a lista precisa estar ordenada
posicao = busca_binaria(numeros, 47)
print(posicao)
