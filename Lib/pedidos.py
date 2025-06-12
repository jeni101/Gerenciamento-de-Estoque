from Lib.Estoque_Cadastro_Salvar import ler_arquivo, salvar_cadastro
import json
import os

DATAWAY = "database/Relatorios_de_saida.json"

def fazer_pedido():
    lista_de_produtos = []

    nome = input("Informe seu nome: ")
    data_solicitacao = input("Digite a data que está sendo feita a solicitação: ")

    while True:
        produto = input("Digite o nome do produto (ou '0' para sair): ").strip()
        if produto == "0":
            break

        try:
            quantidade = float(input(f"Digite a quantidade de '{produto}' em kg: "))
        except ValueError:
            print("Quantidade inválida. Use apenas números.")
            continue

        lista_de_produtos.append((produto, quantidade))

    estoque = ler_arquivo()  # supondo que retorna dict

    for nome_produto, quantidade in lista_de_produtos:
        engradado_encontrado = False

        for linha in estoque.values():
            for pilha in linha.values():
                for engradado in pilha:
                    if engradado["Produto"].lower() == nome_produto.lower():
                        if engradado["peso"] >= quantidade:
                            engradado["peso"] -= quantidade
                            if engradado["peso"] <= 0:
                                pilha.remove(engradado)
                            print(f"Pedido de {quantidade}kg de {nome_produto} atendido com sucesso.")
                        
                        else:
                            print(f"Engradado de {nome_produto} possui apenas {engradado['peso']}kg. Pedido não atendido.")
                        engradado_encontrado = True
                        break
                if engradado_encontrado:
                    break
            if engradado_encontrado:
                break

        if not engradado_encontrado:
            print(f"Produto '{nome_produto}' não encontrado no estoque.")

    # Atualiza o estoque no arquivo
    with open("database/Estoque.json", "w", encoding="utf-8") as f:
        json.dump(estoque, f, ensure_ascii=False, indent=4)

    print("Pedido processado e estoque atualizado.")

    # Monta o pedido para salvar
    pedido = {
        "Nome": nome,
        "Produtos": [{"Produto": p, "Quantidade kg": q} for p, q in lista_de_produtos],
        "Data do Pedido": data_solicitacao
    }

    salvar_pedido(pedido)


def salvar_pedido(pedido):
    if os.path.exists(DATAWAY):
        with open(DATAWAY, 'r', encoding='utf-8') as f:
            try:
                pedidos = json.load(f)
            except json.JSONDecodeError:
                pedidos = []
    else:
        pedidos = []

    # Adiciona o pedido novo na lista
    pedidos.append(pedido)

    with open(DATAWAY, 'w', encoding='utf-8') as f:
        json.dump(pedidos, f, ensure_ascii=False, indent=4)
