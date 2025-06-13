from Lib.Util_Limpar_tela import *
from Lib.Estoque_Cadastro import *
from Lib.View_Mascara import *
from Lib.Presenter_Listar_Produto import *
from Lib.Presenter_Salvar_CodigoBaras import *
from Lib.pedidos import *
from Lib.Listar_pedidos import *

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def view_menu_estoque():
    while True:
        Mascara()
        print("""
   • O que Desejas Verificar?
 |==================================================|
 | -=-                 ESTOQUE                  -=- |
 |==================================================|
 |- Cadastrar Produto ao Estoque  . . . . . . |  1  |
 |- Remover Produto do Estoque  . . . . . . . |  2  |
 |- Visualizar Estoque  . . . . . . . . . . . |  3  |
 |____________________________________________|_____|
 |- Voltar  . . . . . . . . . . . . . . . . . |  0  |
 |==================================================| 
""")
        try:
            escolha = int(input("   • Digite Sua Escolha: "))
        except ValueError:
            Mascara()
            print("   • Opção Não Válida, Tente Novamente: ")
            continue

        match escolha:
            case 1:
                Mascara()
                buscar_info_produto()
                break
            
            case 2:
                Mascara()
                confirmar_remover()
                break
            
            case 3:
                Mascara()
                buscar_produto_por_nome()
                break
            
            case 0:
                Mascara()
                return

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
            Mascara()
            print("   • Opção Não Válida, Tente Novamente: ")
            continue

        match escolha:
            case 1:
                Mascara()
                fazer_pedido()
                
                break
            
            case 2:
                Mascara()
                listar_pedidos()
                break
            
            case 0:
                Mascara()
                return

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def view_menu_relatorios():
    while True:
        print("""
   • Vamos Ver Como Está Rolando as Coisas?
 |==================================================|
 | -=-               RELATORIOS                 -=- |
 |==================================================|
 |- Gerar Novo Relatório de Pedidos . . . . . |  1  |
 |- Visualizar Relatorios . . . . . . . . . . |  2  |
 |- Limpar Relatórios Antigos . . . . . . . . |  3  |
 |____________________________________________|_____|
 |- Voltar  . . . . . . . . . . . . . . . . . |  0  |
 |==================================================| 
""")
        try:
            escolha = int(input("   • Digite Sua Escolha: "))
        except ValueError:
            Mascara()
            print("   • Opção Não Válida, Tente Novamente: ")
            continue

        match escolha:
            case 1:
                Mascara()
                listar_pedidos()
                break
            
            case 2:
                Mascara()
                # Linkar Função que Visualiza Relatorios
                break
            
            case 3:
                Mascara()
                # Linkar Função que Limpa Relatórios Antigos
                break
            
            case 0:
                Mascara()
                return

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# def view_menu_registros():
#     while True:
#         print("""
#    • Aqui Está Tudo Bem Registrado!
#  |==================================================|
#  | -=-                REGISTROS                 -=- |
#  |==================================================|
#  |- Realizar Novo Registro  . . . . . . . . . |  1  |
#  |- Visualizar Histórico de Registros . . . . |  1  |
#  |- Limpar Registros Antigos  . . . . . . . . |  3  |
#  |____________________________________________|_____|
#  |- Voltar  . . . . . . . . . . . . . . . . . |  0  |
#  |==================================================| 
# """)
#         try:
#             escolha = int(input("   • Digite Sua Escolha: "))
#         except ValueError:
#             Mascara()
#             print("   • Opção Não Válida, Tente Novamente: ")
#             continue

#         match escolha:
#             case 1:
#                 Mascara()
#                 # Linkar Função que Visualiza Histórico
#                 break
            
#             case 2:
#                 Mascara()
#                 # Linkar Função que Limpa Registros
#                 break
            
#             case 3:
#                 Mascara()
#                 # Linkar Função que Limpa Registros Antigos
#                 break
            
#             case 0:
#                 Mascara()
#                 return
