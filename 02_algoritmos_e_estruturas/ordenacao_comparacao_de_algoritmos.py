"""
Comparação de algoritmos de ordenação: Selection, Insertion e Bubble sort.

Cada função devolve a lista ordenada + quantas COMPARAÇÕES e TROCAS fez,
para vermos qual algoritmo trabalha menos com a mesma lista.
"""
import random

# 200 números sorteados entre 1 e 299, sem repetição
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
        if menor != i:   # só conta troca se o menor não já estava no lugar certo
            lista[i], lista[menor] = lista[menor], lista[i]
            trocas += 1
    return lista, comparacoes, trocas

# INSERTION_SORT: encaixa um item por vez na parte já ordenada
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


# BUBBLE_SORT: compara vizinhos e troca os que estão fora de ordem
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


# .copy() garante que cada algoritmo ordene a lista original (e não uma já ordenada)
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