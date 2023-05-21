import readTxt
import convertInput
def fusaoVertice(graph, v1, v2):
    # Verifica se os vértices estão presentes no grafo
    if v1 not in graph or v2 not in graph:
        return "Um ou ambos os vértices não estão presentes no grafo"
    
    # Cria um novo vértice com o nome da concatenação dos dois vértices
    new_vertex = v1 + v2
    
    # Adiciona o novo vértice ao grafo
    graph[new_vertex] = set()
    
    # Adiciona as arestas do vértice v1 ao novo vértice
    for neighbor in graph[v1]:
        if neighbor != v2:
            graph[new_vertex].add(neighbor)
            graph[neighbor].add(new_vertex)
    
    # Adiciona as arestas do vértice v2 ao novo vértice
    for neighbor in graph[v2]:
        if neighbor != v1:
            graph[new_vertex].add(neighbor)
            graph[neighbor].add(new_vertex)
    
    # Remove os vértices antigos do grafo
    del graph[v1]
    del graph[v2]
    
    # Remove as arestas dos vértices antigos
    for vertex in graph:
        if v1 in graph[vertex]:
            graph[vertex].remove(v1)
        if v2 in graph[vertex]:
            graph[vertex].remove(v2)
    
    return graph


def result(nameTxt, v1, v2):
  input_str = readTxt.readTxt(nameTxt)
  graph = convertInput.convert_input_to_set(input_str)
  new_graph = fusaoVertice(graph, v1, v2)
  print(new_graph)
