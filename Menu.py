from Controller import saudacao, criarcliente, criarplano, Contratar, relatorio, cancelamento, update

def menu ():
    menu = 1

    while menu != 2:
        saudacao()
        var = int(input('''\nDigite:\n1 para cadastrar novo cliente\n2 para cadastrar novo plano
3 para realizar uma venda\n4 para emitir relatório de clientes\n5 para cancelamento\n6 para atualização de plano\n>>'''))

        match var:
            
            case 1:
                cliente = {}

                cliente["Nome"] = input("\nNome completo:\n>>")
                cliente["Endereço"] = input("\nEndereco:\n>>")
                cliente["Telefone"] = input("\nTelefone:\n>>")
                cliente["Email"] = input("\nEmail:\n>>")

                criarcliente(cliente)
            case 2:
                plano = {}

                plano["Download"] = input("\nDigite a velocidade de download:\n>>")
                plano["Upload"] = input("\nDigite a velocidade de upload:\n>>")
                plano["Valor"] = float(input("\nDigite o valor:\n>>"))

                criarplano(plano)
            case 3:
                Contratar()

            case 4:
                relatorio()

            case 5:
                pessoa = input("\nInforme o nome do cliente que deseja cancelar:\n>>")
                cancelamento(pessoa)

            case 6:
                update()

        menu = int(input("\nGostaria de realizar uma nova operação? Digite:\n1 para sim\n2 para sair\n>>"))