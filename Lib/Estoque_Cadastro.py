from Lib.View_Mascara import *
from Lib.Estoque_Remocao import *

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

global sair 
sair = False

def mensagem_inicial():  # apresentação do sistema
    Mascara()
    print("Bem-vindo ao gerenciador de estoque, escolha a opção:")
    print("""
          1 - Cadastrar produtos
          2 - remover engradado
          """)
    opcao = input(" ")
    if opcao == "1":
        cadastro_de_produtos()
    elif opcao == "2":
        remover_engradado()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def cadastro_de_produtos():# todos os dados que foram requisitados
        
    while sair == False:
        Mascara()
        
        
        categoria = ["Alimenticio", "Higiene", "Casa"]  # exemplo de tipos de categorias

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
        for i, cat in enumerate(categoria, start=1):  # enumerar as categorias disponíveis e pegar na lista
            print(f"{i} - {cat}")
        print("0 - Outro")  # outro caso não tenha na lista, obs: se não tiver, adicionar na lista

        opcao = input("")

        if opcao == "0":
            nova_categoria = input("Digite a nova categoria: ")
            categoria_escolhida = nova_categoria
        elif opcao.lower() == "x":
            return
        else:
            categoria_escolhida = categoria[int(opcao) - 1]  # se tiver a categoria vai pegar aqui (-1 pq o índice começa com 0)

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
        Mascara()
        confirmacao()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    
def confirmacao():
    global sair
    while not sair:
        escolha = input("deseja continuar? (s/n)")
        if escolha.lower() == "s":
            break
        elif escolha.lower() == "n":
            print("voltando....")
            sair = True
        else:
            print("comando invalido, tente novamente.")
            continue

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-