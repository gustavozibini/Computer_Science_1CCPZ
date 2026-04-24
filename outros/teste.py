# 1. O usuário digita 2 valores
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Mostrando os valores em binário para facilitar a conferência visual
print(f"\n-> Binário do 1º número: {num1:b}")
print(f"-> Binário do 2º número: {num2:b}\n")

# 3. Realiza as duas operações lógicas
resultado_and = num1 & num2
resultado_or = num1 | num2

# 2. Converte para binário e fatia para tirar o "0b"
bin_and = bin(resultado_and)[2:]
bin_or = bin(resultado_or)[2:]

# Exibe os resultados
print(f"Resultado da operação AND (&): {bin_and}")
print(f"Resultado da operação OR (|):  {bin_or}")