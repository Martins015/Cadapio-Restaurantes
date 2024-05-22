# Cardápio de Restaurantes

## Descrição 
- O cardápio de restaurantes é um projeto criado em Python que consome uma API com diversos itens de variados restaurantes e organiza em formato de cardápio. O projeto utiliza orientação a objeto como estrutura base.
- Créditos da API: https://github.com/guilhermeonrails

## Funcionalidade
- Mostrar o cardápio de vários restaurantes, incluindo McDonald's, KFC e entre outros.

## Dependências e Instalações
- Para rodar a aplicação, é necessário ter instalado alguns pré-requisitos, conforme mostra abaixo: 
    - Interpretador do Python 3.12 ou posterior;
    - Biblioteca utilizada: Entrar no escopo principal do projeto pelo terminal e colocar o seguinte comando: pip install -r requirements.txt .
      
<div align = "center">
    <img src = "https://github.com/Martins015/Cardapio-Restaurantes/assets/112978196/52db4ea6-249c-4715-bd50-db6bf3fa1591" widt = 150px height = 150px/>
</div>

## Uso

### Rodando o projeto
- Para rodar o projeto, é necessário somente seguir esses passo:
  - Entrar no escopo principal do projeto pelo terminal;
  - Digitar o seguinte comando: python app.py.

### Interface 
- Após rodar o projeto, o terminal será limpo e aparecerá um menú com 7 opções de escolha.

<div align = "center">
    <img src="https://github.com/Martins015/Cardapio-Restaurantes/assets/112978196/a4bc86be-6fb7-4cb6-8ca9-50a32a412871"/>
</div>

- A escolha de 1 a 6 mostrará o cardápio do seu respectivo restaurante, já a 7 encerra o programa.
- Quando escolher o restaurante, a tela será limpa e mostrará o cardápio do restaurante.

<div align = "center">
    <img src = "https://github.com/Martins015/Cardapio-Restaurantes/assets/112978196/f5821294-aa00-4080-897a-f881f942ddaf" widt = 250px, height = 350px/>
    <br/>
</div>

- Na parte inferior da tela, terá uma aba para voltar ao menu, onde é necessário apenas clicar "Enter" para voltar.

<div align = "center">
    <img src = "https://github.com/Martins015/Cardapio-Restaurantes/assets/112978196/23563f6d-633c-4352-b452-a6e29ce2ea1e" widt = 250px, height = 400px/>
</div>

- Dessa forma, poderá navegar entre os cardápios facilmente!

## Estrutura do projeto
- O projeto utilizou uma estrutura de pastas e arquivos que divide as funcionalidades das classes e da comunicação da API em diretórios separados, com o objetivo de deixar o código mais limpo!
- Também utilizei o ambiente virtual nativo do Python para realizar os desenvolvimentos, o Venv! Ele me permitiu criar um ambiente separado que não exigia que eu instalasse as bibliotecas para todos os projetos.

- Segue abaixo uma imagem da estrutura base dos diretórios:
<div align = "center">
    <img src = "https://github.com/Martins015/Cardapio-Restaurantes/assets/112978196/d92a9f75-d91b-4978-93d2-170648123b08" />
</div>

### Diretório API:
- Descrição: O diretório "API" Guarda o arquivo "DataCollect.py", responsável por realizar a conexão com a API e tratativa/organização dos dados.
    <div align = "center">
        <img src = "https://github.com/Martins015/Cardapio-Restaurantes/assets/112978196/c471228b-c254-484e-afa9-8d57fe26b00b"/>
    </div>

    - #### DataCollect.py:
        - O arquivo utiliza da biblioteca "requests" realizar a conexão com a API, utilizando a variável de conexão "dados" para futuras tratativas.
        <div align = "center">
            <img src = "https://github.com/Martins015/Cardapio-Restaurantes/assets/112978196/ba74d0ee-96ca-4bfc-ad16-ba5d5c9f0be6"/>
        </div>
    
        - Após realizar uma verificação no status da conexão, o arquivo obtém os dados em json fornecidos pela API e guarda dentro de uma variável.
    
        - Então, é criado um loop For para separar organizar os itens dos cardápios por restaurantes, pois antes os itens eram divididos individualmente, como mostra o exemplo abaixo :
        <div align = "center">
            <img src = "https://github.com/Martins015/Cardapio-Restaurantes/assets/112978196/00c88bf4-bf9d-4a6e-bf2b-f2ce9bfe5946"/>
            <br/>
        </div>
        
        - Agora pertencem a uma lista que separa os itens por restaurantes: 
            <div align = "center">
                <img src = "https://github.com/Martins015/Cardapio-Restaurantes/assets/112978196/a9c23cad-1906-41dc-820c-d14cfca5bf3f"/>
            </div>
    
        - Assim tornando mais fácil a tratativa de dados em outros arquivos!

- ### Diretório Classes:
    - Descrição: O diretório "Classes" é responsável por armazenar as estruturas de classes utilizadas no projeto. Caso deseje contribuir com o projeto e precise criar um classe, aloque
nesse diretório.

    <div align = "center">
        <br/>
        <img src = "https://github.com/Martins015/Cardapio-Restaurantes/assets/112978196/de34c320-2674-42d2-ba4c-79f24583c536"/>
    </div>
        
    - #### restaurante.py: 
        - O arquivo é responsável por estruturar a classe "restaurante", utilizada no projeto. Na classe são utilizados métodos getter e setter para evitar a tratativa direta dos atributos em outros arquivos. 
        <div align = "center">
            <br/>
            <img src = "https://github.com/Martins015/Cardapio-Restaurantes/assets/112978196/32e9f60d-8dd3-4ee7-805a-f3f4a04ffc90"/>
        </div>
    
        - Atributos: "Nome" -> Responsável por guardar o nome do restaurante | "Itens" -> Lista que guarda os itens do cardápio do restaurante.
       
        - Método adicionar_item: Método setter que cria um dicionário dentro do atributo "Itens", que receberá os valores "Item" (referencía o nome do item), "Preco" e "Descricao". A lista possui uma auto-incrementação, o que permite adicionar vários itens em sequência.
       
        - Método listar_itens: Método getter que mostra todos os itens do cardápio do restaurante de modo formatado na tela, para facilitar a visualização.

- ### CreateClasses.py
    - Descrição: É um arquivo que serve para instânciar as classes nos objetos de cada restaurante da API e alocar os itens de cada restaurante dentro dos objetos.
      
    <div align = "center">
        <br/>
        <img src = "https://github.com/Martins015/Cardapio-Restaurantes/assets/112978196/d7b81afa-7743-4904-a8f8-0718f13e8b9f" height = "500px"/>
    </div>

    - A API retorna itens de 6 restaurantes diferentes, sendo eles: McDonald’s, Pizza Hut, Taco Bell, KFC, Wendy’s e Burger King.
 
    - Então, foi criado a função "adicionarItens" que recebe um objeto como parâmetro. Ela pega o atributo "nome" do objeto (que precisa ser uma instância da classe "Restaurante") e cria
um loop For para pegar cada item do restaurante na lista "dados_restaurante" (criado no diretório /API/DataCollect.py) e chama o método "adicionar_item" do objeto para incrementar  cada informação do item do loop.
 
    - Abaixo da declaração da função, são criados todos os objetos com seus respectivos nomes dos restaurantes. Após cada instânciamento, a função é chamada para adicionar os itens.

- ### app.py
    - Descrição: É o arquivo principal do projeto, que cria o menú de navegação para os cardápios.
      
    <div align = "center">
        <br/>
        <img src = "https://github.com/Martins015/Cardapio-Restaurantes/assets/112978196/689b3b0a-b41d-4313-8f18-ca614440eded" height = "500px"/>
    </div>

     - Nesse arquivo é criado a função "listar_cardapio" que recebe um objeto como parâmetro. Ela é responsável por formatar a tela e mostrar o cardápio do restaurante selecionado pelo usuário.

     - Abaixo da função, temos um menú de escolhas (1 a 7) dentro de um loop While True, que mostra o cardápio do restaurante escolhido e finaliza quando a opção 7 for selecionada. 

