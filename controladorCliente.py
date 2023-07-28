from email.mime import base
import os.path
import json


def gravarClienteJSON():
      with open('cliente.json', 'w') as arqJson:
            json.dump(baseCliente, arqJson, indent=4)


def lerClienteJSON():
      with open('cliente.json', 'r+')as arqJson:
            global baseCliente
            baseCliente =json.load(arqJson)


baseCliente= {}


def cadastrarCliente():
    if os.path.isfile('cliente.json'):
        lerClienteJSON()
    else:
        gravarClienteJSON()
    print("\n")
    print("\n{:^75}".format(">>>>>>>>>>>>>> CADASTRAR CLIENTE <<<<<<<<<<<<<<"))
    print("{:-^80}".format(''))
    cliente = {}
    lerClienteJSON()
    while True:
        cpf = input("Digite o CPF: ")
        if verificarcpf(cpf):
            print("CPF já Cadastrado.")
            input()
            break
        nome = input("Digite o Nome: ")
        endereco = input("Digite o Endereço: ")
        celular = input("Digite o Celular/Telefone: ")
        email = input("Digite o Email: ")
        cliente = {'CPF':cpf, 'Nome':nome, 'Endereço':endereco, 'Celular':celular, 'email':email}
        baseCliente[cpf] = cliente
        gravarClienteJSON()

        opcao = int(input("\nDeseja Cadastrar outro Cliente [1]-Sim [2]-Não : "))
        if opcao != 1:
            break


def verificarcpf(cpf):
    return(cpf in baseCliente)
    

def listarClientes():
    if os.path.isfile('cliente.json'):
        lerClienteJSON()
    else:
        gravarClienteJSON()
    print('\n')
    print('\n{:^110}'.format('>>>>>>>>>>>>>>>>>>>>>>>> LISTAR CLIENTES <<<<<<<<<<<<<<<<<<<<<<<<'))
    print('{:-^110}'.format(''))
    print('{:<13}{:<22}{:<25}{:<22}{:<22}'.format('CPF', 'NOME', 'ENDEREÇO', 'CELULAR/TELEFONE', 'EMAIL'))
    print('{:-^110}'.format(''))
    if len (baseCliente) == 0:
        input("\nBase de dados do cliente vazia!")
        input("\nAperte ENTER para Continuar.")
    else:
        for cliente in baseCliente.values():
            print('{:<13}{:<22}{:<25}{:<22}{:<22}'.format(cliente.get('CPF'), cliente.get('Nome'), cliente.get('Endereço'), cliente.get('Celular'), cliente.get('email')))   
        print('\n{:-^110}'.format(''))
        input("\nAperte ENTER para Continuar.")
    
    

def editarCliente():
    if os.path.isfile('cliente.json'):
        lerClienteJSON()
    else:
        gravarClienteJSON()
    print('\n')
    print('\n{:^110}'.format(">>>>>>>>>>>>>>>>>>>>>>>> EDITAR CLIENTE <<<<<<<<<<<<<<<<<<<<<<<<"))
    print('{:-^110}'.format(''))
    cpf = input("Digite o CPF: ")
    if verificarcpf(cpf):
            for cliente in baseCliente.values():
                if cliente.get('CPF') == cpf:
                    print(('-' * 110))
                    print('{:<13}{:<22}{:<25}{:<22}{:<22}'.format('CPF', 'NOME', 'ENDEREÇO', 'CELULAR/TELEFONE', 'EMAIL'))
                    print('{:<13}{:<22}{:<25}{:<22}{:<22}'.format(cliente.get('CPF'), cliente.get('Nome'), cliente.get('Endereço'), cliente.get('Celular'), cliente.get('email')))   
                    print(('-' * 110))
                    
                    opcao=int(input("\nDeseja Editar esse Cadastro [1]-Sim [2]-Não: "))
                    if opcao == 1:
                        nome = input("Digite o Nome: ")
                        endereco = input("Digite o Endereço: ")
                        celular = input("Digite o Celular/Telefone: ")
                        email = input("Digite o Email: ")
                        cliente = {'CPF':cpf, 'Nome':nome, 'Endereço':endereco, 'Celular':celular, 'email':email}
                        baseCliente[cpf] = cliente
                        print("\nCadastro Editado com Sucesso!!")
                        gravarClienteJSON()
                        input("Aperte ENTER para Continuar.")
                        break
                        
                    elif opcao == 2:
                        break
                    
    else:
        print("\nCPF não Encontrado.")
        input("Aperte ENTER para Continuar.")
        return


def removerCliente():
    if os.path.isfile('cliente.json'):
        lerClienteJSON()
    else:
        gravarClienteJSON()
    print('\n')
    print("\n{:^110}".format(">>>>>>>>>>>>>>>>>>>>>>>> REMOVER CLIENTE <<<<<<<<<<<<<<<<<<<<<<<<"))
    print("{:-^110}".format(''))
    cpf = input("Digite o CPF: ")
    if verificarcpf(cpf):
        for cliente in baseCliente.values():
            if cliente.get('CPF') == cpf:
                print(('-' * 110))
                print('{:<13}{:<22}{:<25}{:<22}{:<22}'.format('CPF', 'NOME', 'ENDEREÇO', 'CELULAR/TELEFONE', 'EMAIL'))
                print('{:<13}{:<22}{:<25}{:<22}{:<22}'.format(cliente.get('CPF'), cliente.get('Nome'), cliente.get('Endereço'), cliente.get('Celular'), cliente.get('email')))   
                print(('-' * 110))
                
                opcao = int(input("\nTem Certeza que Deseja Excluir esse Cadastro [1]-Sim [2]-Não: "))
                if opcao == 1:
                    del baseCliente[cpf]
                    print("\nCadastro Excluído com Sucesso!!")
                    gravarClienteJSON()
                    input("Aperte ENTER para continuar.")
                    return
                else:
                    return
    else:
        print("\nCPF não Encontrado.")
        input("Aperte ENTER para Continuar.")
        return


def buscarCliente():
    if os.path.isfile('cliente.json'):
        lerClienteJSON()
    else:
        gravarClienteJSON()
    print("\n")
    print("\n{:^110}".format(">>>>>>>>>>>>>>>>>>>>>>>> BUSCAR CLIENTE <<<<<<<<<<<<<<<<<<<<<<<<"))
    print("{:-^110}".format(''))
    cpf = input("Digite o CPF: ")
    if verificarcpf(cpf):
        for cliente in baseCliente.values():
            if cliente.get('CPF') == cpf:
                print(('-' * 110))
                print('{:<13}{:<22}{:<25}{:<22}{:<22}'.format('CPF', 'NOME', 'ENDEREÇO', 'CELULAR/TELEFONE', 'EMAIL'))
                print('{:<13}{:<22}{:<25}{:<22}{:<22}'.format(cliente.get('CPF'), cliente.get('Nome'), cliente.get('Endereço'), cliente.get('Celular'), cliente.get('email')))   
                print(('-' * 110))
                input("\nAperte ENTER para Continuar.")
    else:
        print("\nCPF não Encontrado.")
        input("Aperte ENTER para Continuar.")


def buscarClienteVenda(cpf):
    if verificarcpf(cpf):
        for cliente in baseCliente.values():
            if cliente.get('CPF') == cpf:
                clienteNome = cliente.get('Nome')
                return clienteNome
    else:
        print("\nCPF não Encontrado.")
        input("Aperte ENTER para Continuar.")
        return "N/A"



def menuCliente():
    while True:
        print("\n")
        print("*********** MENU CLIENTE ***********")
        print(" [1] - CADASTRAR CLIENTE")
        print(" [2] - LISTAR CLIENTES")
        print(" [3] - EDITAR CLIENTE")
        print(" [4] - REMOVER CLIENTE")
        print(" [5] - BUSCAR CLIENTE")
        print(" [6] - SAIR")
        opcao = int(input("Digite a Opção: "))
    
        if opcao == 1:
            cadastrarCliente()
        elif opcao == 2:
            listarClientes()
        elif opcao == 3:
            editarCliente()
        elif opcao == 4:
            removerCliente()
        elif opcao == 5:
            buscarCliente()
        elif opcao == 6:    
            print("Aplicação Finalizada!!")
            break
        else:
            print("Opção Inválida. Por favor, tente novamente!!")
