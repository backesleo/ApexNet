from datetime import datetime

def saudacao():
    hora= datetime.now(tz=None)
    if hora.hour >= 5 and hora.hour < 13:
        print('''Bom dia! Bem -vindo ao sistema ApexNet.\n
Escolha  qual operação deseja realizar:\n''')
        
    elif hora.hour >= 13 and hora.hour < 18:
        print('''Boa tarde! Bem -vindo ao sistema ApexNet.\n
Escolha  qual operação deseja realizar:\n''')
        
    else:
        print('''Boa noite! Bem -vindo ao sistema ApexNet.\n
Escolha  qual operação deseja realizar:\n''')


def relatorio():
    with open('Contratos.txt', 'r') as arquivo:
        print(arquivo.read())

def criarcliente(cliente):
    with open("clientes.txt", "a") as arquivo:
        arquivo.write (str(cliente)+"\n")
        
def criarplano(plano):
    with open("planos.txt", "a") as arquivo:
        arquivo.write (str(plano)+"\n")


def Contratar(contrato):
    with open('clientes.txt','r') as arquivo:
        lines = arquivo.readlines()
        

        for line in lines:
            
            if contrato == eval(line)["Nome"]:

                with open('Contratos.txt','a') as arquivo:
                    arquivo.write(str(contrato) + '\n')
            
            else:
                print("Cliente não encontrado")



    
        

        

"""def Contratar():
    menu = 1

    while menu != 0:

        var = int(input("Digite:\n1 para escolher o cliente\n2 para escolher o plano\n>>"))

        match var:

            case 1:
                with open('clientes.txt', 'r') as arquivo:
                
                    for line in arquivo:
                    
                        cliente = input("Digite o nome do Cliente\n>>")
                        if cliente == eval(line)["Nome"] in arquivo:

                            with open('Contratos.txt','a') as arquivo:
                                arquivo.write(str(cliente) + '\n')
                arquivo.close()
                return var
                
                

            case 2:
                with open('planos.txt', 'r') as arquivo:
                
                    for line in arquivo:
                    
                        plano = input("Digite o Plano\n>>")
                        if cliente == eval(line)["Download"] in arquivo:

                            with open('Contratos.txt','a') as arquivo:
                                arquivo.write(str(plano) + '\n')
                arquivo.close()

        menu = int(input("Digite 0 para encerrar"))"""

    
    

"""
def Contratar():
    for line in arquivo:
        index +=1

        if Cliente == eval(line)["Nome"] and Plano == eval(line)["Download"]:
            index = 1
            flag = 1

        arquivo.close()

    if flag == 0:
        print("Cliente não encontrado")

    else:

        try:
            with open('clientes.txt','planos.txt' 'r') as arquivo:
                arquivo.readlines()
                

                with open('Contratos.txt', 'a') as arquivo:
                    arquivo.write(str(Cliente, Plano) + '\n')
                    print("Plano contratado com sucesso!!")

        except: 
            print("Erro no sistema")"""