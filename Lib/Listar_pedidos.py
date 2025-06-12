import os 
import json
DATAWAY = "database/Relatorios_de_saida.json"


def listar_pedidos():
    if not os.path.exists(DATAWAY):
        print("Nenhum pedido registrado ainda.")
        return

    with open(DATAWAY, 'r', encoding='utf-8') as f:
        try:
            pedidos = json.load(f)
        except json.JSONDecodeError:
            print("Arquivo de pedidos está vazio ou corrompido.")
            return

    if not pedidos:
        print("Nenhum pedido registrado ainda.")
        return

    print("\n--- LISTA DE PEDIDOS ---\n")
    for i, pedido in enumerate(pedidos, start=1):
        print(f"Pedido #{i}")
        print(f"Nome: {pedido.get('Nome', 'Desconhecido')}")
        print(f"Data do Pedido: {pedido.get('Data do Pedido', 'Não informada')}")
        print("Produtos:")
        for produto in pedido.get("Produtos", []):
            nome_produto = produto.get("Produto", "Produto não informado")
            quantidade = produto.get("Quantidade kg", "Quantidade não informada")
            print(f"  - {nome_produto}: {quantidade} kg")
        print("-" * 30)
