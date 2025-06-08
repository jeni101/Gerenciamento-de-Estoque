from Lib.Estoque_Cadastro_Salvar import *

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def confirmar_remover():
    
    ler_arquivo()
    escolha = input("deseja remover algum engradado do seu estoque? (s/n)")
    if escolha.lowera() == "s":
        pass
    elif escolha.lower() == "n":
        print("voltando....")
        return
    else:
        print("resposta invalida, tente novamente.")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def remover_engradado(estrutura, nome_produto, caminho=""):
    if isinstance(estrutura, dict):
        for chave, valor in estrutura.items():
            novo_caminho = f"{caminho} > {chave}" if caminho else chave
            resultado = remover_engradado(valor, nome_produto, novo_caminho)
            if resultado:
                return resultado

    elif isinstance(estrutura, list):
        for i, item in enumerate(estrutura):
            if isinstance(item, dict) and item.get("Produto") == nome_produto:
                print(f"\nProduto encontrado em: {caminho}")
                print("Dados do engradado:", item)
                certeza = input("Tem certeza que deseja deletar esse produto? (s/n): ")
                if certeza.lower() == "s":
                    del estrutura[i]
                    print("Produto removido com sucesso.")
                    return {"Removido": True, "Localizacao": caminho}
                else:
                    print("Remoção cancelada.")
                    return {"Removido": False}

    return None

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

import json

# Carregue o estoque
with open("database/Estoque.json", "r", encoding="utf-8") as f:
    estoque = json.load(f)

# Pergunte só uma vez

nome = input("Digite o nome do produto para remoção: ")
# Tente remover
resultado = remover_engradado(estoque, nome)

# Salve se algo foi removido
if resultado and resultado.get("Removido"):
    with open("database/Estoque.json", "w", encoding="utf-8") as f:
        json.dump(estoque, f, ensure_ascii=False, indent=4)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-