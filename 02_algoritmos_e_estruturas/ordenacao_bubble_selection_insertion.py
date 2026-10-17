"""
Três algoritmos clássicos de ordenação, lado a lado:
  - Bubble sort:    compara vizinhos e troca se estiverem fora de ordem
  - Selection sort: procura o menor item e coloca na primeira posição livre
  - Insertion sort: pega um item por vez e "encaixa" na posição certa
"""

numeros = [5, 3, 8, 2]

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        # a cada volta, o maior item "sobe" para o fim; por isso o -i
        for j in range(0, n-1-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]   # troca os dois de lugar
    return lista

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        menor = i                          # guarda a posição do menor item encontrado
        for j in range(i+1, n):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista

def insertion_sort(lista):
    for i in range(1, len(lista)):
        atual = lista[i]                   # item que vamos encaixar
        j = i-1
        while j >= 0 and lista[j] > atual:
            lista[j+1] = lista[j]          # empurra os maiores para a direita
            j -= 1
        lista[j+1] = atual
    return lista

# .copy() é importante: cada algoritmo ordena a SUA cópia da lista original.
# (Sem isso, o primeiro já deixaria a lista ordenada para os outros.)
print("bubble_sort")
print(bubble_sort(numeros.copy()))
print("selection_sort:")
print(selection_sort(numeros.copy()))
print("insertion_sort:")
print(insertion_sort(numeros.copy()))
