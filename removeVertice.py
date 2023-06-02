import readTxt
def removeVertice(graph, vertex):
    if vertex in graph:
        del graph[vertex]
    for v in graph:
        if vertex in graph[v]:
            graph[v].remove(vertex)
    return graph

def result(nameTxt, vertex):
    try:
        graph = readTxt.readTxt(nameTxt)
        result = removeVertice(graph, vertex)
        print(result)
    except:
        print("Erro: Arquivo não encontrado")
