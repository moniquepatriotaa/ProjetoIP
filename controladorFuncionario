import os.path
import json


def gravarFuncionarioJSON():
      with open('funcionario.json', 'w') as arqJson:
            json.dump(baseFuncionario, arqJson, indent=4)


def lerFuncionarioJSON():
      with open('funcionario.json', 'r+') as arqJson:
            global baseFuncionario
            baseFuncionario =json.load(arqJson)


baseFuncionario = {}


def cadastrarFuncionario():
    if os.path.isfile('funcionario.json'):
        lerFuncionarioJSON()
    else:
        gravarFuncionarioJSON()
    print("\n")
    print("\n{:^75}".format(">>>>>>>>>>>>>> CADASTRAR FUNCIONÁRIO <<<<<<<<<<<<<<"))
    print("{:-^80}".format(''))
    funcionario = {}
    lerFuncionarioJSON()
    while True:
        cpf = input("Digite o CPF: ")
        if verificarcpf(cpf):
            print("CPF já Cadastrado.")
            input()
            break
        nome = input("Digite o Nome: ")
        mercado = input("Digite o Mercado: ")
        salario = float(input("Digite o Salário: "))
        funcionario = {'CPF':cpf, 'Nome':nome, 'Mercado':mercado, 'Salário':salario}
        baseFuncionario[cpf] = funcionario
        gravarFuncionarioJSON()

        opcao = int(input("\nDeseja Cadastrar outro Funcionário [1]-Sim [2]-Não : "))
        if opcao != 1:
            break


def verificarcpf(cpf):
    return(cpf in baseFuncionario)
    

def listarFuncionarios():
    if os.path.isfile('funcionario.json'):
        lerFuncionarioJSON()
    else:
        lerFuncionarioJSON()
    print('\n')
    print('\n{:^70}'.format('>>>>>>>>>>>>>> LISTAR FUNCIONÁROS <<<<<<<<<<<<<<'))
    print('{:-^70}'.format(''))
    print('{:<13}{:<22}{:<22}{:<13}'.format('CPF', 'NOME', 'MERCADO', 'SALÁRIO'))
    print('{:-^70}'.format(''))
    for funcionario in baseFuncionario.values():
        print('{:<13}{:<22}{:<22}{:<13}'.format(funcionario.get('CPF'), funcionario.get('Nome'), funcionario.get('Mercado'), funcionario.get('Salário')))   
    print('\n{:-^70}'.format(''))
    input("\nAperte ENTER para Continuar.")
    

def editarFuncionario():
    if os.path.isfile('funcionario.json'):
        lerFuncionarioJSON()
    else:
        lerFuncionarioJSON()
    print('\n')
    print('\n{:^70}'.format(">>>>>>>>>>>>>> EDITAR FUNCIONÁRIO <<<<<<<<<<<<<<"))
    print('{:-^70}'.format(''))
    cpf = input("Digite o CPF: ")
    if verificarcpf(cpf):
            for funcionario in baseFuncionario.values():
                if funcionario.get('CPF') == cpf:
                    print(('_' * 70))
                    print('{:<13}{:<22}{:<22}{:<13}'.format('CPF', 'NOME', 'MERCADO', 'SALÁRIO'))
                    print('{:<13}{:<22}{:<22}{:<13}'.format(funcionario.get('CPF'), funcionario.get('Nome'), funcionario.get('Mercado'), funcionario.get('Salário')))
                    print(('_' * 70))
                    
                    opcao=int(input("\nDeseja Editar esse Cadastro [1]-Sim [2]-Não: "))
                    if opcao == 1:
                        nome = input("Digite o Nome: ")
                        mercado = input("Digite o Mercado: ")
                        salario = float(input("Digite o Salário: "))
                        funcionario = {'CPF':cpf, 'Nome':nome, 'Mercado':mercado, 'Salário':salario}
                        baseFuncionario[cpf] = funcionario
                        print("\nCadastro Editado com Sucesso!!")
                        gravarFuncionarioJSON()
                        input("Aperte ENTER para Continuar.")
                        break
                        
                    elif opcao == 2:
                        break
                    
    else:
        print("\nCPF não Encontrado.")
        input("Aperte ENTER para Continuar.")
        return


def removerFuncionario():
    if os.path.isfile('funcionario.json'):
        lerFuncionarioJSON()
    else:
        lerFuncionarioJSON()
    print('\n')
    print("\n{:^70}".format(">>>>>>>>>>>>>> REMOVER FUNCIONÁRIO <<<<<<<<<<<<<<"))
    print("{:-^70}".format(''))
    cpf = input("Digite o CPF: ")
    if verificarcpf(cpf):
        for funcionario in baseFuncionario.values():
            if funcionario.get('CPF') == cpf:
                print(('_' * 70))
                print('{:<13}{:<22}{:<22}{:<13}'.format('CPF', 'NOME', 'MERCADO', 'SALÁRIO'))
                print('{:<13}{:<22}{:<22}{:<13}'.format(funcionario.get('CPF'), funcionario.get('Nome'), funcionario.get('Mercado'), funcionario.get('Salário')))
                print(('_' * 70))
                
                opcao = int(input("\nTem Certeza que Deseja Excluir esse Cadastro [1]-Sim [2]-Não: "))
                if opcao == 1:
                    del baseFuncionario[cpf]
                    print("\nCadastro Excluído com Sucesso!!")
                    gravarFuncionarioJSON()
                    input("Aperte ENTER para continuar.")
                    return
                else:
                    return
    else:
        print("\nCPF não Encontrado.")
        input("Aperte ENTER para Continuar.")
        return


def buscarFuncionario():
    if os.path.isfile('funcionario.json'):
        lerFuncionarioJSON()
    else:
        lerFuncionarioJSON()
    print("\n")
    print("\n{:^70}".format(">>>>>>>>>>>>>> BUSCAR FUNCIONÁRIO <<<<<<<<<<<<<<"))
    print("{:-^70}".format(''))
    cpf = input("Digite o CPF: ")
    if verificarcpf(cpf):
        for funcionario in baseFuncionario.values():
            if funcionario.get('CPF') == cpf:
                print(('_' * 70))
                print('{:<13}{:<22}{:<22}{:<13}'.format('CPF', 'NOME', 'MERCADO', 'SALÁRIO'))
                print('{:<13}{:<22}{:<22}{:<13}'.format(funcionario.get('CPF'), funcionario.get('Nome'), funcionario.get('Mercado'), funcionario.get('Salário')))
                print(('_' * 70))
                input("\nAperte ENTER para Continuar.")
    else:
        print("\nCPF não Encontrado.")
        input("Aperte ENTER para Continuar.")


def buscarFuncionarioVenda(cpf):
    if verificarcpf(cpf):
        for funcionario in baseFuncionario.values():
            if funcionario.get('CPF') == cpf:
                funcionarioNome = funcionario.get('Nome')
                return funcionarioNome
    else:
        print("\nCPF não Encontrado.")
        input("Aperte ENTER para Continuar.")
        return "N/A"


def menuFuncionario():
    while True:
        print("\n")
        print("*********** MENU FUNCIONÁRIO ***********")
        print(" [1] - CADASTRAR FUNCIONÁRIO")
        print(" [2] - LISTAR FUNCIONÁRIOS")
        print(" [3] - EDITAR FUNCIONÁRIO")
        print(" [4] - REMOVER FUNCIONÁRIO")
        print(" [5] - BUSCAR FUNCIONÁRIO")
        print(" [6] - SAIR")
        opcao = int(input("Digite a Opção: "))
    
        if opcao == 1:
            cadastrarFuncionario()
        elif opcao == 2:
            listarFuncionarios()
        elif opcao == 3:
            editarFuncionario()
        elif opcao == 4:
            removerFuncionario()
        elif opcao == 5:
            buscarFuncionario()
        elif opcao == 6:    
            print("Aplicação Finalizada!!")
            break
        else:
            print("Opção Inválida. Por favor, tente novamente!!")

