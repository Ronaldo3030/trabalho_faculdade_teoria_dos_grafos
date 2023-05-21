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

# Exemplo de uso
grafo = {
    'A': ['B', 'C', 'D', 'S'],
    'B': ['A', 'C', 'D', 'S'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'B', 'C', 'S'],
    'S': ['A', 'B', 'D']
}

grafo = contract_edge(grafo, ('A', 'B'))
print(grafo)
