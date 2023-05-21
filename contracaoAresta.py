import readTxt
import convertInput
def contract_edge(graph, edge):
    u, v = edge
    # Verifica se a aresta existe no grafo
    if v not in graph[u]:
        return graph
    # Mescla os vizinhos de v em u
    for neighbor in graph[v]:
        if neighbor != u:
            graph[u].append(neighbor)
            graph[neighbor].remove(v)
            graph[neighbor].append(u)
    # Remove v do grafo
    del graph[v]
    # Remove a aresta (u,v) do grafo
    graph[u].remove(v)
    return graph

def result(nameTxt, v1, v2):
  input_str = readTxt.readTxt(nameTxt)
  graph = convertInput.convert_input_to_set(input_str)
  new_graph = contract_edge(graph, (v1, v2))
  print(new_graph)