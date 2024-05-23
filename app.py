from CreateClasses import mcDonalds, pizzaHut, tacoBell, kfc, wendys, burguerKing
import os


def listar_cardapio(obj):
    os.system('cls')
    obj.listar_itens()
    input('\nPressione enter para voltar ao início:')
    inicio()

def inicio():
    os.system('cls')
    print('-' * 30)
    print('Cardápio restaurantes'.center(30))
    print('-' * 30)
    print(f'[1] {mcDonalds.Nome}')
    print(f'[2] {pizzaHut.Nome}')
    print(f'[3] {tacoBell.Nome}')
    print(f'[4] {kfc.Nome}')
    print(f'[5] {wendys.Nome}')
    print(f'[6] {burguerKing.Nome}')
    print('[7] Encerrar programa')

    while True:
        escolha = int(input('\nDigite o sua escolha: '))

        match(escolha):
            case 1:
                listar_cardapio(mcDonalds)
            case 2:
                listar_cardapio(pizzaHut)
            case 3:
                listar_cardapio(tacoBell)
            case 4:
                listar_cardapio(kfc)
            case 5:
                listar_cardapio(wendys)
            case 6:
                listar_cardapio(burguerKing)
            case 7:
                os.system('cls')
                exit()
            case __:
                print('Digite um valor válido!\n')
                os.system('cls')


if __name__ == '__main__':
    inicio()