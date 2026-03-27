# #print("hello world!!")
# '''print("hello world!!")'''
# check1 = 9
# check2 = 7.5
# check3 = 8
#
# media = (check1 + check2 + check3)/3
# print(media)
# # print((check1 + check2 + check3)/3)
# print(f"Média = {media:.2f}")
#
#
p_name = input("Digite o nome do produto: ")
p_val = int(input("Digite o valor: "))
p_qty = int(input("Digite a quantidade: "))
p_pct = float(input("Digite a porcentagem de desconto: "))

v_total = p_val * p_qty
v_off = (v_total * p_pct) / 100
v_final = v_total - v_off

print(f"Produto: {p_name}\n"
      f"Valor bruto: R${v_total:.2f}\n"
      f"Desconto: R${v_off:.2f}\n"
      f"Valor final: R${v_final:.2f}")