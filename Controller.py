from datetime import datetime

def saudacao():
    hora= datetime.now(tz=None)
    if hora.hour >= 5 and hora.hour < 13:
        print('''\nBom dia! Bem -vindo ao sistema ApexNet.\n
Escolha  qual operação deseja realizar:\n''')
        
    elif hora.hour >= 13 and hora.hour < 18:
        print('''\nBoa tarde! Bem -vindo ao sistema ApexNet.\n
Escolha  qual operação deseja realizar:\n''')
        
    else:
        print('''\nBoa noite! Bem -vindo ao sistema ApexNet.\n
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


def Contratar():
    clientes = []
    planos = []

    cliente_find = input("\nInforme o nome do cliente:\n>>")

    with open('clientes.txt', 'r') as arquivo_clientes:
        
        for linha in arquivo_clientes:
            
            cliente = eval(linha.strip()) 
            clientes.append(cliente)

    cliente_encontrado = None
    for cliente in clientes:
        if cliente['Nome'] == cliente_find:
            cliente_encontrado = cliente
            break

    if cliente_encontrado == None:
        print("\nCliente não encontrado!\n")
        return

    plano_velocidade = input("\nInforme a velocidade do plano:\n>>")

    with open('planos.txt', 'r')as arquivo_planos:
        
        for linha in arquivo_planos:
            plano = eval(linha.strip())
            planos.append(plano)

    plano_encontrado = None
    for plano in planos:
        if plano['Download'] == plano_velocidade:
            plano_encontrado = plano
            break

    if plano_encontrado == None:
        print("\nPlano não encontrado!\n")
        return

    with open('Contratos.txt', 'a') as arquivo_contratos:
            contrato = {
                'nome': cliente_encontrado['Nome'],
                'plano': plano_encontrado['Download']
            }
            arquivo_contratos.write(str(contrato) + '\n')

    print("\nContrato gerado com sucesso!\n")

def relatorio():
    with open('Contratos.txt', 'r') as arquivo:
        print(arquivo.read())

def cancelamento(cliente):
    index = 0 
    flag = 0
    
    arquivo = open("contratos.txt", "r")

    for line in arquivo:
        index +=1

        if cliente == eval(line)["nome"]:

            chave = index

            flag = 1

    arquivo.close()

    if flag == 0:
        print("\nCliente não encontrado!\n>>")

    else:

        try:
            with open("Contratos.txt", "r") as arquivo:
                lines = arquivo.readlines()

                posicao = 1

                with open("Contratos.txt", "w") as arquivo:
                    for line in lines:
                        if posicao != chave:
                            arquivo.write(line)

                        posicao += 1
            print("\nPlano cancelado com sucesso!\n")
        
        except:
            print("Erro Sistema")



def update():
    clientes = []
    planos = []

    cliente_find = input("\nInforme o nome do cliente:\n>>")

    with open('Contratos.txt', 'r') as arquivo_clientes:
        for linha in arquivo_clientes:
            cliente = eval(linha.strip()) 
            clientes.append(cliente)

    cliente_encontrado = None
    for i, cliente in enumerate(clientes):
        if cliente['nome'] == cliente_find:
            cliente_encontrado = cliente
            break

    if cliente_encontrado is None:
        print("\nCliente não encontrado!\n")
        return

    plano_velocidade = input("\nInforme a velocidade do plano:\n>>")

    with open('planos.txt', 'r') as arquivo_planos:
        for linha in arquivo_planos:
            plano = eval(linha.strip())
            planos.append(plano)

    plano_encontrado = None
    for plano in planos:
        if plano['Download'] == plano_velocidade:
            plano_encontrado = plano
            break

    if plano_encontrado is None:
        print("\nPlano não encontrado!\n")
        return

    with open("Contratos.txt", "r") as arquivo_contratos:
        linhas = arquivo_contratos.readlines()

    with open("Contratos.txt", "w") as arquivo_contratos:
        for i, linha in enumerate(linhas):
            if i == clientes.index(cliente_encontrado):
                contrato = {
                    'nome': cliente_encontrado['nome'],
                    'plano': plano_encontrado['Download']
                }
                arquivo_contratos.write(str(contrato) + '\n')
            else:
                arquivo_contratos.write(linha)

    print("\nCliente atualizado com sucesso!\n")

    



    