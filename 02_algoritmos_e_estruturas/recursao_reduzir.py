"""
Recursão: uma função que chama ela mesma.

Duas versões de "reduzir", para comparar quantas vezes a função é chamada:
  - reduzir:  chama a si mesma UMA vez com n // 2  -> poucas chamadas (cresce devagar)
  - reduzir2: chama a si mesma DUAS vezes          -> o número de chamadas explode
"""

n = 22
def reduzir(n):
    print(n)
    if n <= 1: return        # caso base: sem ele a recursão nunca pararia
    reduzir(n // 2)          # divide n por 2 a cada chamada
reduzir(n)



n = 22
def reduzir2(n):
    if n <= 1:
        return
    reduzir2(n // 2)
    reduzir2(n // 2)         # duas chamadas por nível: bem mais trabalho
reduzir2 (n)
