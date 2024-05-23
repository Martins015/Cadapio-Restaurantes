from API.DataCollect import dados_restaurante
from Classes.restaurante import Restaurante
def adicionarItens(pObjeto):
    for c in dados_restaurante[pObjeto.Nome]:
        pObjeto.adicionar_item(c['Item'], c['Preco'], c['Descricao'])


mcDonalds = Restaurante('McDonald’s')
adicionarItens(mcDonalds)

pizzaHut = Restaurante('Pizza Hut')
adicionarItens(pizzaHut)

tacoBell = Restaurante('Taco Bell')
adicionarItens(tacoBell)

kfc = Restaurante('KFC')
adicionarItens(kfc)

wendys = Restaurante('Wendy’s')
adicionarItens(wendys)

burguerKing = Restaurante('Burger King')
adicionarItens(burguerKing)



