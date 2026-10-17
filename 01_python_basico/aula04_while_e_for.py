"""
Aula 04 - Laços de repetição: while e for.

Quase tudo aqui está comentado (são os exemplos da aula, um por vez).
Só o último exemplo (laços aninhados) está ativo e roda de verdade.
  while: repete ENQUANTO a condição for verdadeira
  for:   repete um número conhecido de vezes (range)
  break: sai do laço   |   continue: pula para a próxima volta
"""

# cp = 0
# while cp < 3:
#     print (f"produto {cp}")
#     cp += 1
#
# i = 4
# while i >=  0:
#     print (i)
#     i -= 1
#
#
# jogar = "sim"
#
# while jogar.lower() == "sim":
#     print("iniciar ou repetir o jogo")
#     jogar = input("deseja jogar novamente? ")
#
# i = 0
# while i < 10:
#     i += 1
#
#     if i == 3 or i == 5:
#         continue
#
#     if i == 7:
#         break
#
#     print(f"produto {i}")
#
#
# n = int(input(" Digite um numero int pos. n: "))
#
# cont = 1
# while cont <= n:
#     print(cont)
#     cont += 1
#
#
# def v_nota(nota):
#     while nota < 0 or nota > 10:
#         print("A nota deve estar entre 0 e 10")
#         nota = float(input("Digite novamente"))
#     return nota
#
#
# n1 = float(input(" nota 1: "))
# n1 = v_nota(n1)
#
# n2 = float(input(" Nota 2: "))
# n2 = v_nota(n2)
#
#
# media = (n1 + n2) / 2
# print(media)

# ===== a partir daqui: laço for =====

# for count_music in range (3):
#     print(f"Musica {count_music}")
#
# for i in range (1, 12, 2):
#     print(i)


# atividade 3
# qtd_m = int(input("Digite a qtd de musica que voce tem na playlist (DB)"))
#
# for i in range(qtd_m):
#     print(f"Musica {i}")
#

# Laços aninhados (um dentro do outro): para cada i, o j roda completo.
# range(0, 3, 2) conta de 0 até 2, pulando de 2 em 2 (só 0 e 2)

for i in range (0, 4):
    for j in range (0, 3, 2 ):
        print(f"i : {i}, j : {j}")
