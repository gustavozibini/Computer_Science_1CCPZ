"""
Calculadora de desconto de um produto.

Pede o nome, o valor, a quantidade e a porcentagem de desconto,
e mostra o valor bruto, o desconto e o valor final.
"""

# Primeiros testes da aula (média de 3 notas), deixados como anotação:
# check1 = 9
# check2 = 7.5
# check3 = 8
#
# media = (check1 + check2 + check3)/3
# print(f"Média = {media:.2f}")  # :.2f mostra só 2 casas decimais

# input() sempre devolve texto, por isso usamos int() e float() para converter em número
p_name = input("Digite o nome do produto: ")
p_val = int(input("Digite o valor: "))
p_qty = int(input("Digite a quantidade: "))
p_pct = float(input("Digite a porcentagem de desconto: "))

# Cálculos: total = valor x quantidade; desconto = porcentagem do total
v_total = p_val * p_qty
v_off = (v_total * p_pct) / 100
v_final = v_total - v_off

# f"..." deixa colocar variáveis dentro do texto usando {}
print(f"Produto: {p_name}\n"
      f"Valor bruto: R${v_total:.2f}\n"
      f"Desconto: R${v_off:.2f}\n"
      f"Valor final: R${v_final:.2f}")
