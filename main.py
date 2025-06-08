from Lib.View_Menus import *
from Lib.Limpar_tela import *

def menu_inicial():
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
        escolha = input("   • Digite Sua Escolha:")
        
        match escolha:
            case "1":
                limpar_tela()
                view_menu_estoque()
                
            case "2":
                limpar_tela()
                view_menu_pedidos()
                
            case "3":
                limpar_tela()
                view_menu_registros()
                
            case "4":
                limpar_tela()
                view_menu_relatorios()
                
            case "0":
                limpar_tela()
                print("   • Até Mais! ")
                break
            
            case _:
                limpar_tela()
                print("   • Opção Não Válida, Tente Novamente:")
                
# Executar Menu Inicial
menu_inicial()