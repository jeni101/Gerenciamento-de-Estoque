import os
import json

DATAWAY = "database/Relatorios_de_saida.json"


def limpar_historico():
    # Sobrescreve o arquivo com uma lista vazia
    with open(DATAWAY, 'w', encoding='utf-8') as f:
        json.dump([], f, ensure_ascii=False, indent=4)
    print("Histórico de pedidos limpo com sucesso.")