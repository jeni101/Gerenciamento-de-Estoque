from Lib.Limpar_tela import *

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def view_menu_estoque():
    while True:
        print("""
   • O que Desejas Verificar?
 |==================================================|
 | -=-                 ESTOQUE                  -=- |
 |==================================================|
 |- Adicionar Produto ao Estoque  . . . . . . |  1  |
 |- Remover Produto do Estoque  . . . . . . . |  2  |
 |- Visualizar Estoque  . . . . . . . . . . . |  3  |
 |____________________________________________|_____|
 |- Voltar  . . . . . . . . . . . . . . . . . |  0  |
 |==================================================| 
""")
        try:
            escolha = int(input("   • Digite Sua Escolha: "))
        except ValueError:
            limpar_tela()
            print("   • Digite um número válido.")
            continue

        match escolha:
            case 1:
                limpar_tela()
                # Linkar Função de Adicionar Produtos ao Estoque
                break
            case 2:
                limpar_tela()
                # Linkar Função que Remove Itens do Estoque
                break
            case 3:
                limpar_tela()
                # Linkar Função que Visualiza o Estoque
                break
            case 0:
                limpar_tela()
                return
            case _:
                limpar_tela()
                print("   • Opção Não Válida, Tente Novamente:")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def view_menu_pedidos():
    while True:
        print("""
   • O que Vamos Pedir Hoje?
 |==================================================|
 | -=-                 PEDIDOS                  -=- |
 |==================================================|
 |- Registrar Novo Pedido . . . . . . . . . . |  1  |
 |- Visualizar Pedidos Ativos . . . . . . . . |  2  |
 |____________________________________________|_____|
 |- Voltar  . . . . . . . . . . . . . . . . . |  0  |
 |==================================================| 
""")
        try:
            escolha = int(input("   • Digite Sua Escolha: "))
        except ValueError:
            limpar_tela()
            print("   • Digite um número válido.")
            continue

        match escolha:
            case 1:
                limpar_tela()
                # Linkar Função de Registrar Novo Pedido
                break
            case 2:
                limpar_tela()
                # Linkar Função que Visualiza Pedidos Ativos
                break
            case 0:
                limpar_tela()
                return
            case _:
                limpar_tela()
                print("   • Opção Não Válida, Tente Novamente:")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def view_menu_registros():
    while True:
        print("""
   • Aqui Está Tudo Bem Registrado!
 |==================================================|
 | -=-                REGISTROS                 -=- |
 |==================================================|
 |- Realizar Novo Registro  . . . . . . . . . |  1  |
 |- Visualizar Histórico de Registros . . . . |  1  |
 |- Limpar Registros Antigos  . . . . . . . . |  3  |
 |____________________________________________|_____|
 |- Voltar  . . . . . . . . . . . . . . . . . |  0  |
 |==================================================| 
""")
        try:
            escolha = int(input("   • Digite Sua Escolha: "))
        except ValueError:
            limpar_tela()
            print("   • Digite um número válido.")
            continue

        match escolha:
            case 1:
                limpar_tela()
                # Linkar Função que Visualiza Histórico
                break
            case 2:
                limpar_tela()
                # Linkar Função que Limpa Registros
                break
            case 3:
                limpar_tela()
                # Linkar Função que Limpa Registros Antigos
                break
            case 0:
                limpar_tela()
                return
            case _:
                limpar_tela()
                print("   • Opção Não Válida, Tente Novamente:")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def view_menu_relatorios():
    while True:
        print("""
   • Vamos Ver Como Está Rolando as Coisas?
 |==================================================|
 | -=-               RELATORIOS                 -=- |
 |==================================================|
 |- Gerar Novo Relatório  . . . . . . . . . . |  1  |
 |- Visualizar Último Relatório . . . . . . . |  2  |
 |- Limpar Relatórios Antigos . . . . . . . . |  3  |
 |____________________________________________|_____|
 |- Voltar  . . . . . . . . . . . . . . . . . |  0  |
 |==================================================| 
""")
        try:
            escolha = int(input("   • Digite Sua Escolha: "))
        except ValueError:
            limpar_tela()
            print("   • Digite um número válido.")
            continue

        match escolha:
            case 1:
                limpar_tela()
                # Linkar Função que Gera Novo Relatório
                break
            case 2:
                limpar_tela()
                # Linkar Função que Visualiza Último Relatório
                break
            case 3:
                limpar_tela()
                # Linkar Função que Limpa Relatórios Antigos
                break
            case 0:
                limpar_tela()
                return
            case _:
                limpar_tela()
                print("   • Opção Não Válida, Tente Novamente:")
