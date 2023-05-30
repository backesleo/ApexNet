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
    clientes = []
    planos = []

    cliente_find = input("Informe o nome do cliente\n>>")

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
        print("Cliente não encontrado!")
        return
    

    plano_velocidade = int(input("Informe a velocidade do plano\n>>"))

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
        print("Plano não encontrado!")
        return

    with open('Contratos.txt', 'a') as arquivo_contratos:
            contrato = {
                'nome': cliente_encontrado['Nome'],
                'plano': plano_encontrado['Download']
            }
            arquivo_contratos.write(str(contrato) + '\n')

    print("Contrato gerado com sucesso!")