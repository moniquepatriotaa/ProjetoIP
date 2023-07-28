import os.path
import json
from datetime import date
from controladorFuncionario import buscarFuncionarioVenda
from controladorCliente import buscarClienteVenda
from controladorProduto import buscarProdutoVenda


def gravarVendasJSON():
      with open('venda.json', 'w') as arqJson:
            json.dump(baseVendas, arqJson, indent=4)


def lerVendasJSON():
      with open('venda.json', 'r+') as arqJson:
            global baseVendas
            baseVendas =json.load(arqJson)


baseVendas = {}


def cadastrarVenda(): 
    if os.path.isfile('venda.json'):
        lerVendasJSON()
    else:
        gravarVendasJSON()
    
    print("\n")
    print("\n{:^75}".format(">>>>>>>>>>>>>> CADASTRAR VENDA <<<<<<<<<<<<<<"))
    print("{:-^80}".format(''))
    venda = {}
    lerVendasJSON()
    while True:
        vendaCodigo = input("Digite o Número da Venda: ")
        if verificarVenda(vendaCodigo):
            print("Venda já Cadastrada.")
            input()
            break
        codigoProduto = input("Digite o Código de Barras: ")
        produto = buscarProdutoVenda(codigoProduto)
        preco = input("Digite o Preço: ")
        cpfClinte = input("Digite o CPF do Cliente: ")
        cliente = buscarClienteVenda(cpfClinte)
        cpfFuncionario = input("Digite o CPF do Funcionario: ")
        funcionario = buscarFuncionarioVenda(cpfFuncionario)
        data = date.today().strftime("%m/%d/%Y")
        print("Data:",data)
        venda = {'Venda':vendaCodigo, 'Codigo':codigoProduto, 'Produto':produto, 'Preço':preco, 'Cliente':cliente, "Funcionario": funcionario, "Data": data}
        baseVendas[vendaCodigo] = venda
        gravarVendasJSON()

        opcao = int(input("\nDeseja Cadastrar outra Venda [1]-Sim [2]-Não : "))
        if opcao != 1:
            break


def verificarVenda(vendaCodigo):
    return(vendaCodigo in baseVendas)
    

def listarVendas():
    if os.path.isfile('venda.json'):
        lerVendasJSON()
    else:
        gravarVendasJSON()
    print('\n')
    print('\n{:^110}'.format('>>>>>>>>>>>>>>>>>>>>> LISTAR VENDAS <<<<<<<<<<<<<<<<<<<<<'))
    print('{:-^140}'.format(''))
    print('{:<20}{:<20}{:<25}{:<20}{:<25}{:<20}{:<20}'.format('VENDA', 'CÓDIGO', 'PRODUTO', 'PREÇO', 'CLIENTE', 'FUNCIONARIO', 'DATA'))
    print('{:-^140}'.format(''))
    for venda in baseVendas.values():
        print('{:<20}{:<20}{:<25}{:<20}{:<25}{:<20}{:<30}'.format(venda.get('Venda'), venda.get('Codigo'), venda.get('Produto'), venda.get('Preço'), venda.get('Cliente'), venda.get('Funcionario'), venda.get('Data'))) 
    print('\n{:-^140}'.format(''))
    data = date.today()
    print("Vendas Realizadas no Dia:",data) 
    input("\nAperte ENTER para Continuar.")

def editarVenda():
    if os.path.isfile('venda.json'):
        lerVendasJSON()
    else:
        gravarVendasJSON()
    print('\n')
    print('\n{:^110}'.format(">>>>>>>>>>>>>>>>>>>>> EDITAR VENDA <<<<<<<<<<<<<<<<<<<<<"))
    print('{:-^140}'.format(''))
    vendaCodigo = input("Digite o Número da Venda: ")
    if verificarVenda(vendaCodigo):
            for venda in baseVendas.values():
                if venda.get('Venda') == vendaCodigo:
                    print(('-' * 140))
                    print('{:<20}{:<20}{:<25}{:<20}{:<25}{:<20}{:<20}'.format('VENDA', 'CÓDIGO', 'PRODUTO', 'PREÇO', 'CLIENTE', 'FUNCIONARIO', 'DATA'))
                    print('{:<20}{:<20}{:<25}{:<20}{:<25}{:<20}{:<20}'.format(venda.get('Venda'), venda.get('Codigo'), venda.get('Produto'), venda.get('Preço'), venda.get('Cliente'), venda.get('Funcionario'), venda.get('Data')))   
                    print(('-' * 140))
                    
                    opcao=int(input("\nDeseja Editar esse Cadastro [1]-Sim [2]-Não: "))
                    if opcao == 1:

                        codigoProduto = input("Digite o Código de Barras: ")
                        produto = input("Digite o Produto: ")
                        preco = input("Digite o Preço: ")
                        cliente = input("Digite o Nome do Cliente: ")
                        data = venda.get('Data')

                        if codigoProduto == None or codigoProduto == '' or codigoProduto == ' ':
                            codigoProduto = venda.get('Codigo')
                            continue
                        elif produto == None or produto == '' or produto == ' ':
                            produto = venda.get('Produto')
                            continue
                        elif preco == None or preco == '' or preco == ' ':
                            preco = venda.get('Preço')
                            continue
                        elif cliente == None or cliente == '' or cliente == ' ':
                            cliente = venda.get('Cliente')
                        

                        venda = {'Venda':vendaCodigo, 'Codigo':codigoProduto, 'Produto':produto, 'Preço':preco, 'Cliente':cliente, "Funcionario": funcionario, "Data": data}
                        baseVendas[vendaCodigo] = venda
                        print("\nCadastro Editado com Sucesso!!")
                        gravarVendasJSON()
                        input("Aperte ENTER para Continuar.")
                        break
                        
                    elif opcao == 2:
                        break
                    
    else:
        print("\nVenda não Encontrada.")
        input("Aperte ENTER para Continuar.")
        return


def removerVenda():
    if os.path.isfile('venda.json'):
        lerVendasJSON()
    else:
        gravarVendasJSON()
    print('\n')
    print("\n{:^110}".format(">>>>>>>>>>>>>>>>>>>>>>>> REMOVER VENDA <<<<<<<<<<<<<<<<<<<<<<<<"))
    print("{:-^140}".format(''))
    vendaCodigo = input("Digite o Número da Venda: ")
    if verificarVenda(vendaCodigo):
            for venda in baseVendas.values():
                if venda.get('Venda') == vendaCodigo:
                    print(('-' * 140))
                    print('{:<20}{:<20}{:<25}{:<20}{:<25}{:<20}{:<20}'.format('VENDA', 'CÓDIGO', 'PRODUTO', 'PREÇO', 'CLIENTE', 'FUNCIONARIO', 'DATA'))
                    print('{:<20}{:<20}{:<25}{:<20}{:<25}{:<20}{:<20}'.format(venda.get('Venda'), venda.get('Codigo'), venda.get('Produto'), venda.get('Preço'), venda.get('Cliente'), venda.get('Funcionario'), venda.get('Data')))   
                    print(('-' * 140))
                
                opcao = int(input("\nTem Certeza que Deseja Excluir esse Cadastro [1]-Sim [2]-Não: "))
                if opcao == 1:
                    del baseVendas[vendaCodigo]
                    print("\nCadastro Excluído com Sucesso!!")
                    gravarVendasJSON()
                    input("Aperte ENTER para continuar.")
                    return
                else:
                    return
    else:
        print("\nVenda não Encontrada.")
        input("Aperte ENTER para Continuar.")
        return


def buscarVenda():
    if os.path.isfile('venda.json'):
        lerVendasJSON()
    else:
        gravarVendasJSON()
    print("\n")
    print("\n{:^100}".format(">>>>>>>>>>>>>>>>>>>>>>>> BUSCAR VENDA <<<<<<<<<<<<<<<<<<<<<<<<"))
    print("{:-^100}".format(''))
    vendaCodigo = input("Digite o Número da Venda: ")
    if verificarVenda(vendaCodigo):
            for venda in baseVendas.values():
                if venda.get('Venda') == vendaCodigo:
                    print(('-' * 140))
                    print('{:<20}{:<20}{:<25}{:<20}{:<25}{:<20}{:<20}'.format('VENDA', 'CÓDIGO', 'PRODUTO', 'PREÇO', 'CLIENTE', 'FUNCIONARIO', 'DATA'))
                    print('{:<20}{:<20}{:<25}{:<20}{:<25}{:<20}{:<20}'.format(venda.get('Venda'), venda.get('Codigo'), venda.get('Produto'), venda.get('Preço'), venda.get('Cliente'), venda.get('Funcionario'), venda.get('Data')))   
                    print(('-' * 140))
                    input("\nAperte ENTER para Continuar.")
    else:
        print("\nVenda não Encontrada.")
        input("Aperte ENTER para Continuar.")


def menuVenda():
    while True:
        print("\n")
        print("*********** MENU VENDAS ***********")
        print(" [1] - CADASTRAR VENDA")
        print(" [2] - LISTAR VENDAS")
        print(" [3] - EDITAR VENDA")
        print(" [4] - REMOVER VENDA")
        print(" [5] - BUSCAR VENDA")
        print(" [6] - SAIR")
        opcao = int(input("Digite a Opção: "))
    
        if opcao == 1:
            cadastrarVenda()
        elif opcao == 2:
            listarVendas()
        elif opcao == 3:
            editarVenda()
        elif opcao == 4:
            removerVenda()
        elif opcao == 5:
            buscarVenda()
        elif opcao == 6:    
            print("Aplicação Finalizada!!")
            break
        else:
            print("Opção Inválida. Por favor, tente novamente!!")
