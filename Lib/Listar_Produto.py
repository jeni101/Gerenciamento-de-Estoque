from Lib.Estoque_Cadastro_Salvar import *


def buscar_produto_por_nome():
    
    nome_buscado = input("Digite o nome do produto que deseja buscar: ")

    # Verifica se o arquivo existe
    if not os.path.exists(DATAWAY):
        print("Arquivo de estoque não encontrado.")
        return

    # Tenta abrir e ler o arquivo
    with open(DATAWAY, 'r', encoding='utf-8') as f:
        try:
            estoque = json.load(f)
        except json.JSONDecodeError:
            print("Erro ao ler o estoque.")
            return

    encontrado = False

    # Percorre cada linha
    for linha_nome, pilhas in estoque.items():
        # Percorre cada pilha
        for pilha_nome, produtos in pilhas.items():
            # Percorre os produtos dentro da pilha
            for produto in produtos:
                if produto.get("Produto", "").lower() == nome_buscado.lower():
                    print(f"\n Produto encontrado em {linha_nome} > {pilha_nome}:")
                    for chave, valor in produto.items():
                        print(f"{chave}: {valor}")
                    encontrado = True

    if not encontrado:
        print("Produto não encontrado.")
