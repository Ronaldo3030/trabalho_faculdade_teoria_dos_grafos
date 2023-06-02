def readTxt(nameFile):
    try:
        with open(nameFile, 'r') as arquivo:
            conteudo = arquivo.read()
            grafo = {}
            for linha in conteudo.split('\n'):
                if linha:
                    linha = linha.rstrip(';')
                    no, vizinhos = linha.split(':')
                    grafo[no] = vizinhos.split(',')
            return grafo
    except:
        print("Erro: Arquivo não encontrado")