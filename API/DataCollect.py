import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
dados = requests.get(url)

if dados.status_code == 200:
    dados_json = dados.json()
    dados_restaurante = {}
    for c in dados_json:
        if c['Company'] not in dados_restaurante:
            dados_restaurante[c['Company']] = []

        dados_restaurante[c['Company']].append({
            'Item': c['Item'],
            'Preco': c['price'],
            'Descricao': c['description']
        })
