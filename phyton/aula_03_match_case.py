escolha_usuario = int(input('Digite: '))

match escolha_usuario:
    case 0:
        print('Entrar no programa')
    case 1:
        print('sair no programa')
    case _:
        print('erro')