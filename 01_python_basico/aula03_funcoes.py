"""Aula 03 - Funções: blocos de código reutilizáveis, criados com def."""

# Exemplo antigo, guardado como anotação (função sem parâmetro):
# def print_lyrics():
#     print("Que vai querer a minha perikita")
#     print("Que vai querer a minha perikita")
#     print("Que vai querer a minha perikita")
#
# print_lyrics()


# Função com PARÂMETRO: "nome" recebe o valor que for passado na chamada
def welcome(nome):
    print(f"Ola, {nome} seja bem vindo")

nome_digitado = input("Digite seu nome: ")
welcome(nome_digitado)

# Função com RETORNO: devolve um resultado que pode ser guardado numa variável
def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

resultado = soma(7,5)
print(resultado)
print(type(nome_digitado))  # type() mostra o tipo do dado (aqui: str, texto)
