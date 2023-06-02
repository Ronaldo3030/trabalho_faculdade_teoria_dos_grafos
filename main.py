import algKahn
import belman
import djikstra
import preOrdem
import posOrdem
import emOrdem
import removeNode
import fusaoVertice
import contracaoVertice
import contracaoAresta

def main():
    while True:
        print("-----------------------------------------------------------")
        print("Escolha uma opção:")
        print("1. Impressão em Pré-Ordem")
        print("2. Impressão Pós-Ordem")
        print("3. Impressão EmOrdem")
        print("4. Remoção de um vértice de uma árvore")
        print("5. Fusão de dois vértices")
        print("6. Contração de um vértice")
        print("7. Contração de uma aresta")
        print("8. Ordenação Topológica (algoritmo de Kahn)")
        print("9. Caminho Mínimo - Dijkstra")
        print("10. Caminho Mínimo - Bellman-Ford")
        print("11. Sair do programa")
        print("-----------------------------------------------------------")
        opcao = input("Digite sua escolha: ")
        # PASSANDO COMO PARAMENTRO:
        # NOME DO ARQUIVO TXT, VERTICES A MANIPULAR
        if opcao == '1':
            print("-----------------------------------------------------------")
            getRoute = input("Informe o caminho do arquivo: ")
            print("-----------------------------------------------------------")
            print("-----------------------------------------------------------")
            raiz = input("Informe o nó raiz: ")
            print("-----------------------------------------------------------")
            if(getRoute != '' and raiz != ''):
                print("##########################################################")
                preOrdem.result(getRoute, raiz)
                print("##########################################################")
            else:
                print("Opção inválida. Voltando ao menu principal!")
        elif opcao == '2':
            print("-----------------------------------------------------------")
            getRoute = input("Informe o caminho do arquivo: ")
            print("-----------------------------------------------------------")
            print("-----------------------------------------------------------")
            raiz = input("Informe o nó raiz: ")
            print("-----------------------------------------------------------")
            if(getRoute != '' and raiz != ''):
                print("##########################################################")
                posOrdem.result(getRoute, raiz)
                print("##########################################################")
            else:
                print("Opção inválida. Voltando ao menu principal!")
        elif opcao == '3':
            print("-----------------------------------------------------------")
            getRoute = input("Informe o caminho do arquivo: ")
            print("-----------------------------------------------------------")
            print("-----------------------------------------------------------")
            raiz = input("Informe o nó raiz: ")
            print("-----------------------------------------------------------")
            if(getRoute != '' and raiz != ''):
                print("##########################################################")
                emOrdem.result(getRoute, raiz)
                print("##########################################################")
            else:
                print("Opção inválida. Voltando ao menu principal!")
        elif opcao == '4':
            print("-----------------------------------------------------------")
            getRoute = input("Informe o caminho do arquivo: ")
            print("-----------------------------------------------------------")
            print("-----------------------------------------------------------")
            raiz = input("Informe o que deseja remover: ")
            print("-----------------------------------------------------------")
            if(getRoute != '' and raiz != ''):
                print("##########################################################")
                removeNode.result(getRoute, raiz)
                print("##########################################################")
            else:
                print("Opção inválida. Voltando ao menu principal!")
        elif opcao == '5':
            print("-----------------------------------------------------------")
            getRoute = input("Informe o caminho do arquivo: ")
            print("-----------------------------------------------------------")
            print("-----------------------------------------------------------")
            v1 = input("Informe o primeiro vertice: ")
            print("-----------------------------------------------------------")
            print("-----------------------------------------------------------")
            v2 = input("Informe o segundo vertice: ")
            print("-----------------------------------------------------------")
            if(getRoute != ''):
                print("##########################################################")
                fusaoVertice.result(getRoute, v1, v2)
                print("##########################################################")
            else:
                print("Opção inválida. Voltando ao menu principal!")
        elif opcao == '6':
            print("-----------------------------------------------------------")
            getRoute = input("Informe o caminho do arquivo: ")
            print("-----------------------------------------------------------")
            print("-----------------------------------------------------------")
            v1 = input("Informe o vertice a ser removido: ")
            print("-----------------------------------------------------------")
            if(getRoute != ''):
                print("##########################################################")
                contracaoVertice.result(getRoute, v1)
                print("##########################################################")
            else:
                print("Opção inválida. Voltando ao menu principal!")
        elif opcao == '7':
            print("-----------------------------------------------------------")
            getRoute = input("Informe o caminho do arquivo: ")
            print("-----------------------------------------------------------")
            print("-----------------------------------------------------------")
            v1 = input("Informe o primeiro vertice: ")
            print("-----------------------------------------------------------")
            print("-----------------------------------------------------------")
            v2 = input("Informe o segundo vertice: ")
            print("-----------------------------------------------------------")
            if(getRoute != ''):
                print("##########################################################")
                contracaoAresta.result(getRoute, v1, v2)
                print("##########################################################")
            else:
                print("Opção inválida. Voltando ao menu principal!")
        elif opcao == '8':
            print("-----------------------------------------------------------")
            getRoute = input("Informe o caminho do arquivo: ")
            print("-----------------------------------------------------------")
            if(getRoute != ''):
                print("##########################################################")
                algKahn.result(getRoute)
                print("##########################################################")
            else:
                print("Opção inválida. Voltando ao menu principal!")
        elif opcao == '9':
            print("-----------------------------------------------------------")
            getRoute = input("Informe o caminho do arquivo: ")
            print("-----------------------------------------------------------")
            print("-----------------------------------------------------------")
            raiz = input("Informe o nó: ")
            print("-----------------------------------------------------------")
            if(getRoute != ''):
                print("##########################################################")
                djikstra.result(getRoute, raiz)
                print("##########################################################")
            else:
                print("Opção inválida. Voltando ao menu principal!")
        elif opcao == '10':
            print("-----------------------------------------------------------")
            getRoute = input("Informe o caminho do arquivo: ")
            print("-----------------------------------------------------------")
            print("-----------------------------------------------------------")
            raiz = input("Informe o nó: ")
            print("-----------------------------------------------------------")
            if(getRoute != ''):
                print("##########################################################")
                belman.result(getRoute, raiz)
                print("##########################################################")
            else:
                print("Opção inválida. Voltando ao menu principal!")
        elif opcao == '11':
            break
        else:
            print("Opção inválida.")


main()
