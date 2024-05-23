class Restaurante():
    def __init__(self, pNome):
        self.Nome = pNome
        self.Itens = []

    def adicionar_item(self, pItem, pPreco, pDescricao):
        self.Itens += [
            {
                'Item': pItem,
                'Preco': pPreco,
                'Descricao': pDescricao
            }
        ]

    def listar_itens(self):
        print('-' * 150)
        print(f'Cardápio {self.Nome}'.center(150))
        print('-' * 150)
        print(f'\n{'Nome'.ljust(50) } | {'Preço'.ljust(7)} | {'Descrição'.ljust(50)}')
        for c in self.Itens:
            print(f'\n{str(c['Item']).ljust(50)} | R${str(c['Preco']).ljust(5)} |  {str(c['Descricao']).ljust(50)}')

