import requests
from Lib.View_Mascara import *
from Lib.Estoque_Cadastro_Salvar import *


sair = False  # não precisa de global aqui se for bem usado nas funções

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def buscar_info_produto(): # API para buscar um produto pelo codigo de barras
    while True:
        Mascara()
        codigo_barras = input("   • Digite o número do código de barras: ")
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

        Mascara()
        print(f"""
 |==============================================================================|
 | -=-                Informações do Produto : {codigo_barras:<28} -=- |
 |==============================================================================|
 |- Nome: {nome:<36}|- Valor Venda:                   |
 |____________________________________________|_________________________________|
 |- Peso: {peso:<26}|- Data de Validade:                        |
 |- Quantidade: {quantidade:<20}|- Data de Fabricação:                      |
 |__________________________________|___________________________________________|
 |- Categoria: {categoria_geral:35}|- Preço de Compra:           |
 |______________________________________________________________________________|
 |- Fabricante:                         |- Fornecedor:                          |
 |______________________________________|______________________________________ |
 |============================================================================= | 
 |- Voltar  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |   0   |
 |============================================================================= | 
 """)

        temp_fabricante = input("   • Nome do Fabricante: ")
        Mascara()
        print(f"""
 |==============================================================================|
 | -=-                Informações do Produto : {codigo_barras:<28} -=- |
 |==============================================================================|
 |- Nome: {nome:<36}|- Valor Venda:                   |
 |____________________________________________|_________________________________|
 |- Peso: {peso:<26}|- Data de Validade:                        |
 |- Quantidade: {quantidade:<20}|- Data de Fabricação:                      |
 |__________________________________|___________________________________________|
 |- Categoria: {categoria_geral:35}|- Preço de Compra:           |
 |______________________________________________________________________________|
 |- Fabricante: {temp_fabricante:<24}|- Fornecedor:                          |
 |______________________________________|______________________________________ |
 |============================================================================= | 
 |- Voltar  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |   0   |
 |============================================================================= | 
 """)

        temp_fornecedor = input("   • Nome do Fornecedor: ")
        Mascara()
        print(f"""
 |==============================================================================|
 | -=-                Informações do Produto : {codigo_barras:<28} -=- |
 |==============================================================================|
 |- Nome: {nome:<36}|- Valor Venda:                   |
 |____________________________________________|_________________________________|
 |- Peso: {peso:<26}|- Data de Validade:                        |
 |- Quantidade: {quantidade:<20}|- Data de Fabricação:                      |
 |__________________________________|___________________________________________|
 |- Categoria: {categoria_geral:35}|- Preço de Compra:           |
 |______________________________________________________________________________|
 |- Fabricante: {temp_fabricante:<24}|- Fornecedor: {temp_fornecedor:<25}|
 |______________________________________|______________________________________ |
 |============================================================================= | 
 |- Voltar  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |   0   |
 |============================================================================= | 
 """)

        temp_validade = input("   • Informe a Data de Validade do Produto (dd/mm/aaaa): ")
        Mascara()
        print(f"""
 |==============================================================================|
 | -=-                Informações do Produto : {codigo_barras:<28} -=- |
 |==============================================================================|
 |- Nome: {nome:<36}|- Valor Venda:                   |
 |____________________________________________|_________________________________|
 |- Peso: {peso:<26}|- Data de Validade: {temp_validade:<23}|
 |- Quantidade: {quantidade:<20}|- Data de Fabricação:                      |
 |__________________________________|___________________________________________|
 |- Categoria: {categoria_geral:35}|- Preço de Compra:           |
 |______________________________________________________________________________|
 |- Fabricante: {temp_fabricante:<24}|- Fornecedor: {temp_fornecedor:<25}|
 |______________________________________|_______________________________________|
 |==============================================================================| 
 |- Voltar  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |   0   |
 |==============================================================================| 
 """)
        
        temp_fabricacao = input("   • Informe a Data de Fabricação do Produto (dd/mm/aaaa): ")
        Mascara()
        print(f"""
 |==============================================================================|
 | -=-                Informações do Produto : {codigo_barras:<28} -=- |
 |==============================================================================|
 |- Nome: {nome:<36}|- Valor Venda:                   |
 |____________________________________________|_________________________________|
 |- Peso: {peso:<26}|- Data de Validade: {temp_validade:<23}|
 |- Quantidade: {quantidade:<20}|- Data de Fabricação: {temp_fabricacao:<21}|
 |__________________________________|___________________________________________|
 |- Categoria: {categoria_geral:35}|- Preço de Compra:           |
 |______________________________________________________________________________|
 |- Fabricante: {temp_fabricante:<24}|- Fornecedor: {temp_fornecedor:<25}|
 |______________________________________|_______________________________________|
 |==============================================================================| 
 |- Voltar  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |   0   |
 |==============================================================================| 
 """)

        temp_precovenda = input("   • Informe o Preço de Venda: ")
        Mascara()
        print(f"""
 |==============================================================================|
 | -=-                Informações do Produto : {codigo_barras:<28} -=- |
 |==============================================================================|
 |- Nome: {nome:<36}|- Valor Venda: {temp_precovenda:<18}|
 |____________________________________________|_________________________________|
 |- Peso: {peso:<26}|- Data de Validade: {temp_validade:<23}|
 |- Quantidade: {quantidade:<20}|- Data de Fabricação: {temp_fabricacao:<21}|
 |__________________________________|___________________________________________|
 |- Categoria: {categoria_geral:35}|- Preço de Compra:           |
 |______________________________________________________________________________|
 |- Fabricante: {temp_fabricante:<24}|- Fornecedor: {temp_fornecedor:<25}|
 |______________________________________|_______________________________________|
 |==============================================================================| 
 |- Voltar  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |   0   |
 |==============================================================================| 
 """)
    
        temp_precocompra = input("   • Informe o Preço de Compra: ")
        Mascara()
        print(f"""
 |==============================================================================|
 | -=-                Informações do Produto : {codigo_barras:<28} -=- |
 |==============================================================================|
 |- Nome: {nome:<36}|- Valor Venda: {temp_precovenda:<18}|
 |____________________________________________|_________________________________|
 |- Peso: {peso:<26}|- Data de Validade: {temp_validade:<23}|
 |- Quantidade: {quantidade:<20}|- Data de Fabricação: {temp_fabricacao:<21}|
 |__________________________________|___________________________________________|
 |- Categoria: {categoria_geral:35}|- Preço de Compra: {temp_precocompra:<10}|
 |______________________________________________________________________________|
 |- Fabricante: {temp_fabricante:<24}|- Fornecedor: {temp_fornecedor:<25}|
 |______________________________________|_______________________________________|
 |==============================================================================| 
 |- Voltar  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |   0   |
 |==============================================================================| 
 """)
    
        # Preenchendo dicionário padrão para edição
        engradado = {
            "Fabricante": temp_fabricante,
            "Fornecedor": temp_fornecedor,
            "Produto": nome,
            "Categoria": categoria_geral,
            "Quantidade": quantidade,
            "Peso": peso,
            "Data_de_Validade": temp_validade,
            "Data_de_Fabricacao": temp_fabricacao,
            "Preco_de_Venda": temp_precovenda,
            "Preco_de_Compra" : temp_precocompra 
        }

        engradados_final = editavel_produtos([engradado])

        # chamar metodo de salvar 
        escolha = input("deseja salvar essa versao? (s/n)").lower()
        if escolha == "s":
            for e in engradados_final:
                salvar_cadastro(e)
            print("Engradados(s) salvos(s) com sucesso.")
        else:
            print("cadastro descartado.")
        
        
        decisao = input("   • Para sair digite '0' + Enter, e para continuar aperte qualquer tecla: ")
        if decisao == "0":
            Mascara()
            break

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def mensagem_de_Aviso(): # a API n é 100% 
    global sair
    while not sair:
        Mascara()
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

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def editavel_produtos(lista_engradados): # edicao das variaveis
 
    resposta = input("Deseja alterar algum valor antes de salvar? (s/n): ").lower()

    if resposta == "s":
        base = lista_engradados[0]  # <- Garantir acesso ao engradado base já no início
        print("""
   • Escolha o Campo que Deseja Alterar:
 |=================================================================|
 | -=-                Alteração de Informações                 -=- |
 |=================================================================|
 |- Fabricante  . . . . . .|  1  |- Peso  . . . . . . . . . .|  7  |
 |- Fornecedor  . . . . . .|  2  |- Data de Validade  . . . .|  8  |
 |- Produto . . . . . . . .|  3  |- Data de Fabricação. . . .|  9  |
 |- Categoria . . . . . . .|  4  |- Preço de Compra . . . . .| 10  |
 |- Quantidade  . . . . . .|  5  |- Preço de Venda  . . . . .| 11  |
 |- Nome  . . . . . . . . .|  6  |-                          |     |
 |_________________________|_____|___________________________|_____|
 |- Voltar  . . . . . . . . . . . . . . . . . . . . . . . . .|  0  |
 |=================================================================| 
""")
        escolha = input("   • Digite sua Escolha:")
        
        # Sempre edita o primeiro engradado da lista (o base)
        base = lista_engradados[0]

        if escolha == "1":
            base["Fabricante"] = input("   • Novo fabricante: ")
        elif escolha == "2":
            base["Fornecedor"] = input("   • Novo fornecedor: ")
        elif escolha == "3":
            base["Produto"] = input("   • Novo nome do produto: ")
        elif escolha == "4":
            base["Categoria"] = input("   • Nova categoria: ")
        elif escolha == "5":
            base["Quantidade"] = input("   • Nova quantidade: ")
        elif escolha == "6":
            base["Nome"] = input("   • Novo Nome: ")
        elif escolha == "7":
            peso_total = int(input("   • Novo peso em kg: "))
            lista_engradados = gerar_engradados_por_peso(base, peso_total) # chama funcao p separar os engradados
            print(f"\nForam gerados {len(lista_engradados)} engradado(s):") # print enumerado do q foi criado com o peso
            for i, j in enumerate(lista_engradados, 1):
                print(f" - Engradado {i}: {j['peso']} kg")
        elif escolha == "8":
            base["Data_de_Validade"] = input("   • Nova data de validade (dd/mm/aaaa): ")
        elif escolha == "9":
            base["Data_de_Fabricacao"] = input("   • Nova data de fabricação (dd/mm/aaaa): ")
        elif escolha == "10":
            base["Preco_de_Compra"] = input("   • Novo preço de compra: ")
        elif escolha == "11":
            base["Preco_de_Venda"] = input("   • Novo preço de venda: ")
        elif escolha == "0":
            print("   • Alterações finalizadas!")
            return lista_engradados
        else:
            print("   • Opção inválida, Tente Novamente.")

        decisao = input("   • Para sair digite '0' + Enter, e para continuar aperte qualquer tecla: ")
        if decisao == "0":
            return lista_engradados
        return editavel_produtos(lista_engradados)  # recursão com o primeiro engradado atualizado

    elif resposta == "n":
        return lista_engradados
    
    # elif resposta.lower() == "n":
    #     escolha = input("Deseja salvar essa versão? (s/n): ").lower()
    #     if escolha == "s":
    #         for e in lista_engradados:
    #             salvar_cadastro(e)
    #         print("Engradados salvos com sucesso!")
    #     else:
    #         print("Engradados não salvos.")
        




def gerar_engradados_por_peso(engradado_base, peso_total): #peso limite limite 100kg 
    engradados = []
    
    quantidade_engradados_cheios = peso_total//100
    
    peso_restante = peso_total % 100
    
    for i in range(quantidade_engradados_cheios):
        novo_engradado = engradado_base.copy()
        novo_engradado["peso"] = 100
        engradados.append(novo_engradado)
    
    if peso_restante > 0:
        restante = engradado_base.copy()
        restante["peso"] = peso_restante
        engradados.append(restante)
    
    return engradados 
        
