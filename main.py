from Lib.cadastro import *
from Lib.View_Menus import *
from Lib.Limpar_tela import *

def mensagem_inicial():
    limpar_tela()    
    while True:
        print("""
   • Bem Vindo ao Menu Inicial!
 |==================================================|
 | -=-                  MENUS                   -=- |
 |==================================================|
 |- Configurações de Estoque  . . . . . . . . |  1  |
 |- Configurações de Pedido . . . . . . . . . |  2  |
 |- Registros . . . . . . . . . . . . . . . . |  3  |
 |- Gerar Relatórios  . . . . . . . . . . . . |  4  |
 |____________________________________________|_____|
 |- Sair. . . . . . . . . . . . . . . . . . . |  0  |
 |==================================================| 
""")
        escolha = input(int("   • Digite Sua Escolha:"))
        match escolha:
            case 1:
                view_menu_estoque()
            case 2:
                view_menu_pedidos()
            case 3:
                view_menu_registros()
            case 4:
                view_menu_relatorios()
            case 0:
                print("   • Até Mais! ")
                break
    pass