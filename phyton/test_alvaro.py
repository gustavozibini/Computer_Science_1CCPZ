import numpy as np
import time
#
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


inicio = time.time()
soma = 0
for i in range (10**6):
    soma += i
fim = time.time()
print(fim - inicio, "segundo")

inicio = time.time()
soma_np = np.sum(np.arange(10**6))
fim = time.time()
print(fim - inicio, "segundo")


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

n = 10**6
inicio = time.time()
soma = n * (n-1) / 2
fim = time.time()
print(fim - inicio, "segundos")
