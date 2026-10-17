"""Aula 03 - Condicionais: if / elif / else decidem qual bloco de código roda."""

nota_final = int(input('Digite a nota final: '))

# O Python testa de cima para baixo e executa só o PRIMEIRO bloco verdadeiro
if nota_final >= 6:
    print('aprovado')
elif nota_final >= 5:
    print('recuperacao')
else:
    print('reprovado')
