import random

numeros = random.sample(range(1, 300), 200)


# SELECTION_SORT
def selection_sort(lista):
    comparacoes = 0
    trocas = 0
    n = len(lista)
    for i in range(n):
        menor = i
        for j in range( i + 1, n):
            comparacoes += 1
            if lista[j] < lista[menor]:
                menor = j
        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]
            trocas += 1
    return lista, comparacoes, trocas

def insertion_sort(lista):
    comparacoes = 0
    trocas = 0
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if lista[j] > atual:
                lista[j + 1] = lista[j]
                j -= 1
                trocas += 1
            else:
                break
        lista[j + 1] = atual
    return lista, comparacoes, trocas


def bubble_sort(lista):
    n = len(lista)
    comparacoes = 0
    trocas = 0
    for i in range(n):
        for j in range(n - 1 - i):
            comparacoes += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
    return lista, comparacoes, trocas


print()
lista, comparacoes, trocas = bubble_sort(numeros.copy())
print("Bubble sort: ", lista)
print("Trocas comparacoes: ", comparacoes)
print("Trocas Realizadas: ", trocas)
print()
lista, comparacoes, trocas = insertion_sort(numeros.copy())
print("Insertion sort: ", lista)
print("Trocas comparacoes: ", comparacoes)
print("Trocas Realizadas: ", trocas)
print()
lista, comparacoes, trocas = selection_sort(numeros.copy())
print("Selection sort: ", lista)
print("Trocas comparacoes: ", comparacoes)
print("Trocas Realizadas: ", trocas)