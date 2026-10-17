"""
Teste de desempenho: quatro jeitos de somar os números de 0 a 999.999,
cronometrando cada um com time.time().

  1. Laço for tradicional
  2. NumPy (opera no vetor inteiro de uma vez)
  3. Laço "desenrolado" (faz 10 somas por volta, menos voltas)
  4. Fórmula matemática (soma de PA), sem laço nenhum -> o mais rápido
"""
import numpy as np
import time

# Versão antiga do teste (sem cronômetro), guardada como anotação:
# # loop tradicional
# soma = 0
# for i in range(10**6):
#     soma += i
# print(soma)
#
#
# # NumPy vetorizado
# soma_np = np.sum(np.arange(10**6))
#
# print(soma_np)


# 1. Laço tradicional
inicio = time.time()
soma = 0
for i in range (10**6):
    soma += i
fim = time.time()
print(fim - inicio, "segundo")

# 2. NumPy
inicio = time.time()
soma_np = np.sum(np.arange(10**6))
fim = time.time()
print(fim - inicio, "segundo")


# 3. Laço desenrolado (loop unrolling): 10 somas por volta, passo de 10 em 10
inicio = time.time()
for i in range (0, 10**6, 10):
    soma += i
    soma += i+1
    soma += i+2
    soma += i+3
    soma += i + 4
    soma += i + 5
    soma += i + 6
    soma += i + 7
    soma += i + 8
    soma += i + 9

fim = time.time()
print(fim - inicio, "segundos")

# 4. Fórmula direta: soma de 0 até n-1 = n * (n-1) / 2
n = 10**6
inicio = time.time()
soma = n * (n-1) / 2
fim = time.time()
print(fim - inicio, "segundos")
