import readTxt
import convertInput
def contract_vertex(graph, v):
    # Verifica se o vértice está presente no grafo
    if v not in graph:
        return "O vértice não está presente no grafo"
    
    # Remove o vértice do grafo
    del graph[v]
    
    # Remove as arestas do vértice
    for vertex in graph:
        if v in graph[vertex]:
            graph[vertex].remove(v)
    
    return graph

def result(nameTxt, v1):
    try:
        input_str = readTxt.readTxt(nameTxt)
        graph = convertInput.convert_input_to_set(input_str)
        new_graph = contract_vertex(graph, v1)
        print(new_graph)
    except:
        print("Erro: Arquivo não encontrado")