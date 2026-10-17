"""Aula 03 - match/case: um jeito de escolher entre várias opções (parecido com vários elif)."""

escolha_usuario = int(input('Digite: '))

match escolha_usuario:
    case 0:
        print('Entrar no programa')
    case 1:
        print('sair no programa')
    case _:  # o "_" vale para qualquer outro valor (é o "else" do match)
        print('erro')
