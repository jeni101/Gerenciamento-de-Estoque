import json
import os
import os.path

DATAWAY = "database/Estoque.json"
DATAWAY_ID = "database/id.json"

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def salvar_cadastro(engradado):  # le o que tem nesse arquivo 
    # Carrega estoque do JSON
    if os.path.exists(DATAWAY):
        with open(DATAWAY, 'r', encoding='utf-8') as f:
            try:
                estoque = json.load(f)
            except json.JSONDecodeError:
                estoque = {}
    else:
        estoque = {}
        
    Numero_ID = atualizar_ID()
    engradado["ID"] = Numero_ID
    
    produto_adicionado = False

    # Tenta adicionar o produto nas pilhas das 8 linhas
    for l in range(1, 9):  # 8 Linhas
        linha_nome = f"Linha_{l}"

        # Se a linha ainda não existir, cria ela
        if linha_nome not in estoque:
            estoque[linha_nome] = {}

        linha = estoque[linha_nome]

        # Dentro de cada linha, tenta adicionar o produto em uma das 5 pilhas
        for p in range(1, 6):  # 5 Pilhas por linha
            pilha_nome = f"Pilha_{p}"

            # Se a pilha não existir na linha, cria ela com o engradado
            if pilha_nome not in linha:
                linha[pilha_nome] = [engradado]
                print(f"Produto adicionado na {linha_nome} > {pilha_nome}")
                produto_adicionado = True
                break
            # Se a pilha existir, mas tiver menos de 5 engradados, adiciona o novo
            elif len(linha[pilha_nome]) < 5:
                linha[pilha_nome].append(engradado)
                print(f"Produto adicionado na {linha_nome} > {pilha_nome}")
                produto_adicionado = True
                break

        # Se o produto foi adicionado, para de procurar em outras linhas e pilhas
        if produto_adicionado:
            break

    # Caso não tenha encontrado espaço para o produto, avisa o usuário
    if not produto_adicionado:
        print("Estoque cheio! Não é possível adicionar mais produtos.")
        return

    # Salva as alterações no arquivo JSON
    with open(DATAWAY, 'w', encoding='utf-8') as f:
        json.dump(estoque, f, ensure_ascii=False, indent=4)

    print("Produto salvo com sucesso!")
    
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    
def ler_arquivo():
    # Carrega estoque do JSON
    if os.path.exists(DATAWAY):
        with open(DATAWAY, 'r', encoding='utf-8') as f:
            try:
                estoque = json.load(f)
            except json.JSONDecodeError:
                estoque = {}
    else:
        estoque = {}
    return estoque # <- lembre de retornar!

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def ler_ID():
    if os.path.exists(DATAWAY_ID):
        with open(DATAWAY_ID, 'r', encoding='utf-8') as f:
            try:
                Numero_ID = json.load(f)
            except json.JSONDecodeError:
                Numero_ID = 0  # Se o arquivo estiver vazio ou corrompido, começa do 0
    else:
        Numero_ID = 0  # Se o arquivo não existir, começa com o ID 0
    return Numero_ID

# Função para atualizar o ID
def atualizar_ID():
    Numero_ID = ler_ID()  # Lê o ID atual
    Numero_ID += 1  # Incrementa o ID
    with open(DATAWAY_ID, 'w', encoding='utf-8') as f:
        json.dump(Numero_ID, f, ensure_ascii=False, indent=4)  # Salva o novo ID
    return Numero_ID
