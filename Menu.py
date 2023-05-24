from Controller import saudacao, criarcliente, criarplano

def menu ():
    menu = 1

    while menu != 0:
        saudacao()
        var = int(input('''Digite:\n1 para cadastrar novo cliente\n2 para cadastrar novo plano
3 para realizar uma venda\n4 para emitir relatório de clientes\n>>'''))

        match var:
            
            case 1:
                cliente = {}

                cliente["Nome"] = input("\nNome completo:\n>>")
                cliente["Endereço"] = input("\nEndereço:\n>>")
                cliente["Telefone"] = input("\nTelefone:\n>>")
                cliente["Email"] = input("\nEmail:\n>>")

                criarcliente(cliente)
            case 2:
                plano = {}

                plano["Download"] = int(input("\nDigite a velocidade de download\n>>"))
                plano["Upload"] = int(input("\nDigite a velocidade de upload\n>>"))
                plano["Valor"] = float(input("\nDigite o valor\n>>"))

                criarplano(plano)
            case 3:
                pass

            case 4:
                pass

        menu = int(input("Gostaria de realizar uma nova operação? Digite:\n1 para sim\n2 para sair"))

menu()