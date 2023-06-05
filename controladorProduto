import os.path
import json


def gravarProdutoJSON():
      with open('produto.json', 'w') as arqJson:
            json.dump(baseProduto, arqJson, indent=4)


def lerProdutoJSON():
      with open('produto.json', 'r+') as arqJson:
            global baseProduto
            baseProduto =json.load(arqJson)


baseProduto= {}


def cadastrarProduto():
    if os.path.isfile('produto.json'):
        lerProdutoJSON()
    else:
        gravarProdutoJSON()
    print("\n")
    print("\n{:^75}".format(">>>>>>>>>>>>>> CADASTRAR PRODUTO <<<<<<<<<<<<<<"))
    print("{:-^80}".format(''))
    produto = {}
    lerProdutoJSON()
    while True:
        codigo = input("Digite o Código de Barras: ")
        if verificarCodigo(codigo):
            print("Código já Cadastrado.")
            input()
            break
        nome = input("Digite o Nome: ")
        peso = input("Digite o Peso: ")
        embalagem = input("Digite a Embalagem: ")
        fornecedor = input("Digite o Fornecedor: ")
        estoque = input("Digite o Estoque: ")
        produto = {'Codigo':codigo, 'Nome':nome, 'Peso':peso, 'Embalagem':embalagem, 'Fornecedor':fornecedor, 'Estoque':estoque}
        baseProduto[codigo] = produto
        gravarProdutoJSON()

        opcao = int(input("\nDeseja Cadastrar outro Produto [1]-Sim [2]-Não : "))
        if opcao != 1:
            break


def verificarCodigo(codigo):
    return(codigo in baseProduto)
    

def listarProdutos():
    if os.path.isfile('produto.json'):
        lerProdutoJSON()
    else:
        gravarProdutoJSON()
    print('\n')
    print('\n{:^100}'.format('>>>>>>>>>>>>>>>>>>>>> LISTAR PRODUTOS <<<<<<<<<<<<<<<<<<<<<'))
    print('{:-^100}'.format(''))
    print('{:<13}{:<22}{:<13}{:<19}{:<22}{:<13}'.format('CÓDIGO', 'NOME', 'PESO', 'EMBALAGEM', 'FORNECEDOR', 'ESTOQUE'))
    print('{:-^100}'.format(''))
    for produto in baseProduto.values():
        print('{:<13}{:<22}{:<13}{:<19}{:<22}{:<13}'.format(produto.get('Codigo'), produto.get('Nome'), produto.get('Peso'), produto.get('Embalagem'), produto.get('Fornecedor'), produto.get('Estoque')))   
    print('\n{:-^100}'.format(''))
    input("\nAperte ENTER para Continuar.")
    
def editarProduto():
    if os.path.isfile('produto.json'):
        lerProdutoJSON()
    else:
        gravarProdutoJSON()
    print('\n')
    print('\n{:^100}'.format(">>>>>>>>>>>>>>>>>>>>> EDITAR PRODUTO <<<<<<<<<<<<<<<<<<<<<"))
    print('{:-^100}'.format(''))
    codigo = input("Digite o Código de Barras: ")
    if verificarCodigo(codigo):
            for produto in baseProduto.values():
                if produto.get('Codigo') == codigo:
                    print(('-' * 100))
                    print('{:<13}{:<22}{:<13}{:<19}{:<22}{:<13}'.format('CÓDIGO', 'NOME', 'PESO', 'EMBALAGEM', 'FORNECEDOR', 'ESTOQUE'))
                    print('{:<13}{:<22}{:<13}{:<19}{:<22}{:<13}'.format(produto.get('Codigo'), produto.get('Nome'), produto.get('Peso'), produto.get('Embalagem'), produto.get('Fornecedor'), produto.get('Estoque')))   
                    print(('-' * 100))
                    
                    opcao=int(input("\nDeseja Editar esse Cadastro [1]-Sim [2]-Não: "))
                    if opcao == 1:
                        nome = input("Digite o Nome: ")
                        peso = input("Digite o Peso: ")
                        embalagem = input("Digite a Embalagem: ")
                        fornecedor = input("Digite o Fornecedor: ")
                        estoque = input("Digite o Estoque: ")
                        produto = {'Codigo':codigo, 'Nome':nome, 'Peso':peso, 'Embalagem':embalagem, 'Fornecedor':fornecedor, 'Estoque':estoque}
                        baseProduto[codigo] = produto
                        print("\nCadastro Editado com Sucesso!!")
                        gravarProdutoJSON()
                        input("Aperte ENTER para Continuar.")
                        break
                        
                    elif opcao == 2:
                        break
                    
    else:
        print("\nCódigo não Encontrado.")
        input("Aperte ENTER para Continuar.")
        return


def removerProduto():
    if os.path.isfile('produto.json'):
        lerProdutoJSON()
    else:
        gravarProdutoJSON()
    print('\n')
    print("\n{:^100}".format(">>>>>>>>>>>>>>>>>>>>>>>> REMOVER PRODUTO <<<<<<<<<<<<<<<<<<<<<<<<"))
    print("{:-^100}".format(''))
    codigo = input("Digite o Código de Barras: ")
    if verificarCodigo(codigo):
            for produto in baseProduto.values():
                if produto.get('Codigo') == codigo:
                    print(('-' * 100))
                    print('{:<13}{:<22}{:<13}{:<19}{:<22}{:<13}'.format('CÓDIGO', 'NOME', 'PESO', 'EMBALAGEM', 'FORNECEDOR', 'ESTOQUE'))
                    print('{:<13}{:<22}{:<13}{:<19}{:<22}{:<13}'.format(produto.get('Codigo'), produto.get('Nome'), produto.get('Peso'), produto.get('Embalagem'), produto.get('Fornecedor'), produto.get('Estoque')))   
                    print(('-' * 100))
                
                opcao = int(input("\nTem Certeza que Deseja Excluir esse Cadastro [1]-Sim [2]-Não: "))
                if opcao == 1:
                    del baseProduto[codigo]
                    print("\nCadastro Excluído com Sucesso!!")
                    gravarProdutoJSON()
                    input("Aperte ENTER para continuar.")
                    return
                else:
                    return
    else:
        print("\nCódigo não Encontrado.")
        input("Aperte ENTER para Continuar.")
        return


def buscarProduto():
    if os.path.isfile('produto.json'):
        lerProdutoJSON()
    else:
        gravarProdutoJSON()
    print("\n")
    print("\n{:^100}".format(">>>>>>>>>>>>>>>>>>>>>>>> BUSCAR PRODUTO <<<<<<<<<<<<<<<<<<<<<<<<"))
    print("{:-^100}".format(''))
    codigo = input("Digite o Código de Barras: ")
    if verificarCodigo(codigo):
            for produto in baseProduto.values():
                if produto.get('Codigo') == codigo:
                    print(('-' * 100))
                    print('{:<13}{:<22}{:<13}{:<19}{:<22}{:<13}'.format('CÓDIGO', 'NOME', 'PESO', 'EMBALAGEM', 'FORNECEDOR', 'ESTOQUE'))
                    print('{:<13}{:<22}{:<13}{:<19}{:<22}{:<13}'.format(produto.get('Codigo'), produto.get('Nome'), produto.get('Peso'), produto.get('Embalagem'), produto.get('Fornecedor'), produto.get('Estoque')))   
                    print(('-' * 100))
                    input("\nAperte ENTER para Continuar.")
    else:
        print("\nCódigo não Encontrado.")
        input("Aperte ENTER para Continuar.")


def buscarProdutoVenda(codigo):
    if os.path.isfile('produto.json'):
        lerProdutoJSON()
    else:
        gravarProdutoJSON()
    if verificarCodigo(codigo):
            for produto in baseProduto.values():
                if produto.get('Codigo') == codigo:
                    produtoNome = produto.get('Nome')
                    return produtoNome
    else:
        print("\nProduto não Encontrado.")
        input("Aperte ENTER para Continuar.")
        return "N/A"



def menuProduto():
    while True:
        print("\n")
        print("*********** MENU PRODUTO ***********")
        print(" [1] - CADASTRAR PRODUTO")
        print(" [2] - LISTAR PRODUTOS")
        print(" [3] - EDITAR PRODUTO")
        print(" [4] - REMOVER PRODUTO")
        print(" [5] - BUSCAR PRODUTO")
        print(" [6] - SAIR")
        opcao = int(input("Digite a Opção: "))
    
        if opcao == 1:
            cadastrarProduto()
        elif opcao == 2:
            listarProdutos()
        elif opcao == 3:
            editarProduto()
        elif opcao == 4:
            removerProduto()
        elif opcao == 5:
            buscarProduto()
        elif opcao == 6:    
            print("Aplicação Finalizada!!")
            break
        else:
            print("Opção Inválida. Por favor, tente novamente!!")
