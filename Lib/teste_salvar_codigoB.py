import requests
from Lib.Util_Limpar_tela import *


sair = False  # não precisa de global aqui se for bem usado nas funções


def buscar_info_produto(): # API para buscar um produto pelo codigo de barras
    while True:
        limpar_tela()
        codigo_barras = input("Digite o número do código de barras: ")
        url = f"https://world.openfoodfacts.org/api/v0/product/{codigo_barras}.json" # uso da url pq da menos erros e tem mais produtos
        response = requests.get(url)

        if response.status_code != 200: 
            print("Erro na requisição.")
            return

        data = response.json()
        if data.get("status") != 1:
            print("Produto não encontrado.")
            return

        produto = data["product"]
        # se tiver mostra oq tem no json se n mostraa outra info
        nome = produto.get("product_name", "Não informado")
        preco = produto.get("price", "Não informado")  # Preço é raro na base
        peso = produto.get("packaging", produto.get("quantity", "Não informado"))
        quantidade = produto.get("quantity", "Não informado") 

        # Tratamento para categoria geral, ser mais compacto, dentro de 1 produto pode haver 100 categorias diferentes
        categorias = produto.get("categories", "")
        lista_categorias = [cat.strip() for cat in categorias.split(",")] if categorias else []
        categoria_geral = lista_categorias[0] if lista_categorias else "Não informado"


        print("\n--- INFORMAÇÕES DO PRODUTO ---")
        print(f"Nome: {nome}")
        print(f"Preço: {preco}")
        print(f"Peso: {peso}")
        print(f"Categoria: {categoria_geral}")
        print(f"Quantidade: {quantidade}")

        # Preenchendo dicionário padrão para edição
        engradado = {
            "Fabricante": input("Fabricante: "),
            "Fornecedor": input("Fornecedor: "),
            "Produto": nome,
            "Categoria": categoria_geral,
            "Quantidade": quantidade,
            "Peso": peso,
            "Data_de_Validade": input("Data de validade (dd/mm/aaaa): "),
            "Data_de_Fabricacao": input("Data de fabricação (dd/mm/aaaa): "),
            "Preco_de_Compra": input("Preço de compra: "),
            "Preco_de_Venda": input("Preço de venda: ")
        }

        mudanca(engradado)

        print("\n--- DADOS FINAIS DO PRODUTO ---")
        for chave, valor in engradado.items():
            print(f"{chave}: {valor}")

        # chamar metodo de salvar 
        
        decisao = input("\nPara sair digite '0' + Enter, e para continuar aperte qualquer tecla: ")
        if decisao == "0":
            break


def mensagem_de_Aviso(): # a API n é 100% 
    global sair
    while not sair:
        limpar_tela()
        escolha = input(
            "Este método de cadastro ainda é meio limitado. Certos produtos podem não ser encontrados por conta de:\n"
            "- Divergência de códigos de barras\n"
            "- Banco de dados desatualizado\n"
            "- Produto não cadastrado\n\n"
            "Tem certeza que deseja continuar? (s/n): "
        )
        if escolha.lower() == "s":
            buscar_info_produto()
            break
        elif escolha.lower() == "n":
            print("Voltando...")
            sair = True
        else:
            print("Opção inválida.")
            continue


def mudanca(engradado): # edicao das variaveis
    resposta = input("\nDeseja alterar algum valor antes de salvar? (s/n): ").lower()

    if resposta == "s":
        print("""
Digite o número do campo que deseja alterar:
  [1] Fabricante
  [2] Fornecedor
  [3] Produto
  [4] Categoria
  [5] Quantidade
  [6] Peso
  [7] Data de Validade
  [8] Data de Fabricação
  [9] Preço de Compra
 [10] Preço de Venda
  [0] Sair
""")
        escolha = input("Escolha: ")

        if escolha == "1":
            engradado["Fabricante"] = input("Novo fabricante: ")
        elif escolha == "2":
            engradado["Fornecedor"] = input("Novo fornecedor: ")
        elif escolha == "3":
            engradado["Produto"] = input("Novo nome do produto: ")
        elif escolha == "4":
            engradado["Categoria"] = input("Nova categoria: ")
        elif escolha == "5":
            engradado["Quantidade"] = input("Nova quantidade: ")
        elif escolha == "6":
            engradado["Peso"] = input("Novo peso: ")
        elif escolha == "7":
            engradado["Data_de_Validade"] = input("Nova data de validade (dd/mm/aaaa): ")
        elif escolha == "8":
            engradado["Data_de_Fabricacao"] = input("Nova data de fabricação (dd/mm/aaaa): ")
        elif escolha == "9":
            engradado["Preco_de_Compra"] = input("Novo preço de compra: ")
        elif escolha == "10":
            engradado["Preco_de_Venda"] = input("Novo preço de venda: ")
        elif escolha == "0":
            print("Alterações finalizadas.")
            return
        else:
            print("Opção inválida.")

        mudanca(engradado)  # recursão

