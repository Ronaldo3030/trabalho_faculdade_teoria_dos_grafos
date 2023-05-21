import preOrdem
import posOrdem
import emOrdem
import removeVertice
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
        print("4. Realize e remoção de um vértice de uma árvore")
        print("5. Realize a Fusão de dois vértices")
        print("6. Realize a Contração de um vértice")
        print("7. Realize a Contração de uma aresta")
        print("8. Realize a Ordenação Topológica (algoritmo de Kahn)")
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
            if(getRoute != ''):
                print("##########################################################")
                preOrdem.result(getRoute, 'A')
                print("##########################################################")
            else:
                print("Opção inválida. Voltando ao menu principal!")
        elif opcao == '2':
            print("-----------------------------------------------------------")
            getRoute = input("Informe o caminho do arquivo: ")
            print("-----------------------------------------------------------")
            if(getRoute != ''):
                print("##########################################################")
                posOrdem.result(getRoute, 'A')
                print("##########################################################")
            else:
                print("Opção inválida. Voltando ao menu principal!")
        elif opcao == '3':
            print("-----------------------------------------------------------")
            getRoute = input("Informe o caminho do arquivo: ")
            print("-----------------------------------------------------------")
            if(getRoute != ''):
                print("##########################################################")
                emOrdem.result(getRoute, 'A')
                print("##########################################################")
            else:
                print("Opção inválida. Voltando ao menu principal!")
        elif opcao == '4':
            print("-----------------------------------------------------------")
            getRoute = input("Informe o caminho do arquivo: ")
            print("-----------------------------------------------------------")
            if(getRoute != ''):
                print("##########################################################")
                removeVertice.result(getRoute, 'A')
                print("##########################################################")
            else:
                print("Opção inválida. Voltando ao menu principal!")
        elif opcao == '5':
            print("-----------------------------------------------------------")
            getRoute = input("Informe o caminho do arquivo: ")
            print("-----------------------------------------------------------")
            if(getRoute != ''):
                print("##########################################################")
                fusaoVertice.result(getRoute, 'A', 'D')
                print("##########################################################")
            else:
                print("Opção inválida. Voltando ao menu principal!")
        elif opcao == '6':
            print("-----------------------------------------------------------")
            getRoute = input("Informe o caminho do arquivo: ")
            print("-----------------------------------------------------------")
            if(getRoute != ''):
                print("##########################################################")
                contracaoVertice.result(getRoute, 'A')
                print("##########################################################")
            else:
                print("Opção inválida. Voltando ao menu principal!")
        elif opcao == '7':
            print("-----------------------------------------------------------")
            getRoute = input("Informe o caminho do arquivo: ")
            print("-----------------------------------------------------------")
            if(getRoute != ''):
                print("##########################################################")
                contracaoAresta.result(getRoute, 'A', 'B')
                print("##########################################################")
            else:
                print("Opção inválida. Voltando ao menu principal!")
        elif opcao == '11':
            break
        else:
            print("Opção inválida.")


main()
