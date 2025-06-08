import json
import os

DATAWAY = "database/dados_produtos.json"

def mensagem_inicial(): # apresentacao do sistema
    print("Bem-vindo ao gerenciador de estoque, escolha a opção:")
    print("1 - Cadastrar produtos")
    opcao = input("> ")
    if opcao == "1":
        cadastro_de_produtos()

def cadastro_de_produtos(): # todos os dados q foram requisitados 
    categoria = ["Alimenticio", "Higiene", "Casa"] # exemplo de tipo de categorias obs: colocar mais tipos 

    fabricante = input("Informe o fabricante: ")
    fornecedor = input("Informe o fornecedor: ")
    nome_produto = input("Nome do produto: ")
    quantidade_produto = input("Quantidade comprada (unidades): ")
    peso_produto = input("Peso do produto (kg por unidade): ")
    data_de_validade = input("Data de validade (dd/mm/aaaa): ")
    data_de_fabricacao = input("Data de fabricação (dd/mm/aaaa): ")
    preco_compra = input("Preço de compra: ")
    preco_venda = input("Preço de venda (unidade): ")

    print("Selecione a categoria do produto:")
    for i, cat in enumerate(categoria, start=1): # enumerar as acategorias disponiveis e pegar na lista
        print(f"{i} - {cat}")
    print("0 - Outro") # outro caso n tenha na lista, obs: se n tiver adicionar na lista

    opcao = input(" ")

    if opcao == "0":
        nova_categoria = input("Digite a nova categoria: ")
        categoria_escolhida = nova_categoria
    else:
        categoria_escolhida = categoria[int(opcao) - 1] # se tiver a categoria vai pegar aqui (-1 pq o indece comeca com 0)

    engradado = {
        "Fabricante": fabricante,
        "Fornecedor": fornecedor,
        "Produto": nome_produto,
        "Categoria": categoria_escolhida,
        "Quantidade": quantidade_produto,
        "Peso": peso_produto,
        "Data_de_Validade": data_de_validade,
        "Data_de_Fabricacao": data_de_fabricacao,
        "Preco_de_Compra": preco_compra,
        "Preco_de_Venda": preco_venda
    }

    salvar_cadastro(engradado)

def salvar_cadastro(engradado): # le oq tem nese arquivo 
    # Carrega estoque do JSON
    if os.path.exists(DATAWAY):
        with open(DATAWAY, 'r', encoding='utf-8') as f:
            try:
                estoque = json.load(f)
            except json.JSONDecodeError:
                estoque = {}
    else:
        estoque = {}

    
    for i in range(1, 41): # tamanho maximo de pilhas 40 possicoes
        pilha_nome = f"pilha_{i}" 
        if pilha_nome not in estoque:
            estoque[pilha_nome] = [engradado] # se n tiver no estoque cria
            print(f"Produto adicionado na nova {pilha_nome}")
            break
        elif len(estoque[pilha_nome]) < 5:      # cada pilha suporta ate 5 engradados 
            estoque[pilha_nome].append(engradado)
            print(f"Produto adicionado na {pilha_nome}")
            break
    else:
        print("Estoque cheio! Não é possível adicionar mais produtos.") # se atingir o limite
        return

    # Salva no JSON
    with open(DATAWAY, 'w', encoding='utf-8') as f:
        json.dump(estoque, f, ensure_ascii=False, indent=4)

    print("Produto salvo com sucesso!")

# Executa

    
    
    
    