from Lib.Estoque_Cadastro_Salvar import *
import json

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def confirmar_remover():
    estoque = ler_arquivo()
    
    escolha = input("Deseja remover algum engradado do seu estoque? (s/n): ").strip().lower()
    if escolha == "s":
        remover(estoque)
    elif escolha == "n":
        print("Voltando...")
    else:
        print("Resposta inválida, tente novamente.")

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def remover_engradado(estrutura, nome_produto, caminho="", removidos=[]):
    if isinstance(estrutura, dict):
        for chave, valor in estrutura.items():
            novo_caminho = f"{caminho} > {chave}" if caminho else chave
            remover_engradado(valor, nome_produto, novo_caminho, removidos)

    elif isinstance(estrutura, list):
        i = 0
        while i < len(estrutura):
            item = estrutura[i]
            if isinstance(item, dict) and item.get("Produto") == nome_produto:
                print(f"\nProduto encontrado em: {caminho}")
                
                print("\nDetalhes do produto:")
                for chave, valor in item.items():
                    print(f"   ▸ {chave}: {valor}")

                
                certeza = input("Tem certeza que deseja deletar este produto? (s/n): ").strip().lower()
                if certeza == "s":
                    removidos.append((caminho, item))
                    del estrutura[i]
                    print("Produto removido com sucesso.")
                    continue  # Não incrementar o índice porque a lista encolheu
                else:
                    print("Remoção cancelada.")
            i += 1
    return removidos

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def remover(estoque=None):
    if estoque is None:
        estoque = ler_arquivo()

    nome = input("Digite o nome do produto para remoção: ").strip()
    removidos = remover_engradado(estoque, nome)

    if removidos:
        with open("database/Estoque.json", "w", encoding="utf-8") as f:
            json.dump(estoque, f, ensure_ascii=False, indent=4)
        print(f"\n {len(removidos)} produto(s) foram removidos com sucesso.")
    else:
        print("Nenhum produto encontrado com esse nome.")