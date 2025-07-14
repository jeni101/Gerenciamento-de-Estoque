from Lib.Util_Limpar_tela import *
def escolha_do_estoque():
    from main import menu_inicial
    while True: 
        limpar_tela()
        
        print("""Este programa conta com um sistema de estoque padrao de 200 posicoes de engradados distribuidos em:
              
5 colunas por 8 linhas, totalizando 40 espacoes e cada espaço comporta um total de 5 engradados:
            
    Estoque: 5 colunas x 8 linhas = 40 espaços
    Cada espaço comporta até 5 engradados

    +-----------+-----------+-----------+-----------+-----------+
    | Esp. 1    | Esp. 2    | Esp. 3    | Esp. 4    | Esp. 5    |
    +-----------+-----------+-----------+-----------+-----------+
    | Esp. 6    | Esp. 7    | Esp. 8    | Esp. 9    | Esp. 10   |
    +-----------+-----------+-----------+-----------+-----------+
    | Esp. 11   | Esp. 12   | Esp. 13   | Esp. 14   | Esp. 15   |
    +-----------+-----------+-----------+-----------+-----------+
    | Esp. 16   | Esp. 17   | Esp. 18   | Esp. 19   | Esp. 20   |
    +-----------+-----------+-----------+-----------+-----------+
    | Esp. 21   | Esp. 22   | Esp. 23   | Esp. 24   | Esp. 25   |
    +-----------+-----------+-----------+-----------+-----------+
    | Esp. 26   | Esp. 27   | Esp. 28   | Esp. 29   | Esp. 30   |
    +-----------+-----------+-----------+-----------+-----------+
    | Esp. 31   | Esp. 32   | Esp. 33   | Esp. 34   | Esp. 35   |
    +-----------+-----------+-----------+-----------+-----------+
    | Esp. 36   | Esp. 37   | Esp. 38   | Esp. 39   | Esp. 40   |
    +-----------+-----------+-----------+-----------+-----------+
            
            """)    
        escolha = input("Caso deseje personalizar essa distibucao deixando ela mais especifica para você digite '1'.\nse deseja continuar com o padrão digite '2': ")
        if escolha =="1":
            mensagem_iformativa()
            resultado()
            
        elif escolha =="2":
            return menu_inicial()
            
        else:
            print("entrada invalida, porfavor insira um numero valido.")







def Linhas():
    linhas = int(input("Linhas:  "))
    return linhas

def Colunas():
    colunas = int(input("Colunas: "))
    return colunas
    
def mensagem_iformativa():
    limpar_tela()
    print("Para um cadastro mais preciso informe a quantidade de espaco disponiveis no seu estoque de\n")
    
def resultado():
    linhas = Linhas()
    colunas = Colunas()
    resultado = linhas * colunas
    posicoes = resultado * 5
    print(f"Você selecionou o molde de {linhas} linhas por {colunas} colunas, totalizando {resultado} espaços e {posicoes} posições disponíveis de engradados para este molde")
    salva = input("deseja continuar com essa estrutura? (s/n)")
    
    
def representacao():
    # print repesentativo dos espacos
    pass