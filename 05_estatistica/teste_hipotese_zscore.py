"""
Teste de hipótese com a distribuição normal (teste Z).

Duas contas:
  Za = valor crítico: o limite que separa "aceitar" de "rejeitar" a hipótese.
       norm.ppf(p) devolve o valor de Z para uma área p da curva normal.
       Com nível de significância de 1% e teste bilateral, usamos p = 0.01 / 2.
  Zc = valor calculado a partir da amostra:
       (média da amostra - média esperada) / (desvio padrão / raiz de n)
       Aqui: média da amostra 395, média esperada 400, desvio 20, amostra de 100.
Regra: se Zc cair além do limite Za (mais extremo que ele), rejeita-se a hipótese.
"""
from math import sqrt
from scipy.stats import norm

# Teste anterior (nível de 5%, teste unilateral), guardado como anotação:
# print("Za = " ,norm.ppf(0.05))
#
# print("Zc=" ,(195 -200) /(10/sqrt(100)))


print("Za = " ,norm.ppf(0.01/2))

print("Zc=" ,(395 -400) /(20/sqrt(100)))
