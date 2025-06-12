
from Lib.View_Menus import *
from Lib.View_Mascara import *
from Lib.Presenter_Salvar_CodigoBaras import *
from Lib.Presenter_Listar_Produto import *
from Lib.pedidos import *



def menu_inicial():
    Mascara()    
    while True:
        print("""
   • Bem Vindo ao Menu Inicial!
 |==================================================|
 | -=-                  MENUS                   -=- |
 |==================================================|
 |- Configurações de Estoque  . . . . . . . . |  1  |
 |- Configurações de Pedido . . . . . . . . . |  2  |
 |- Gerar Relatórios  . . . . . . . . . . . . |  3  |
 |____________________________________________|_____|
 |- Sair. . . . . . . . . . . . . . . . . . . |  0  |
 |==================================================| 
""")
        escolha = input("   • Digite Sua Escolha: ")
        
        match escolha:
            case "1":
                Mascara()
                view_menu_estoque()
                
            case "2":
                Mascara()
                view_menu_pedidos()
                
            case "3":
                Mascara()
                # view_menu_relatorios()
                
            case "0":
                Mascara()
                print("   • Até Mais! ")
                break
            
            case _:
                Mascara()
                print("   • Opção Não Válida, Tente Novamente:")
                
# Executar Menu Inicial
menu_inicial()

