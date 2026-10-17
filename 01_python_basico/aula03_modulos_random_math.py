"""Aula 03 - Módulos: bibliotecas prontas que usamos com import (random, math)."""

# Exemplo do módulo math, guardado como anotação:
# import math
#
# num = 99
# raiz = math.sqrt(num)  # raiz quadrada
#
# print(f"A raiz de {num} é {raiz:.2f}")


import random

# Sorteia um número inteiro entre 1 e 60 (como na Mega-Sena)
num_megasena = random.randint(1,60)

print(num_megasena)
