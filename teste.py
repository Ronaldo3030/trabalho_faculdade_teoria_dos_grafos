import belmanReadTxt
def bellman_ford(graph, V, E, src):
    dist = [float('inf')] * V
    dist[src] = 0

    for i in range(V - 1):
        for j in range(E):
            u, v, w = graph[j]
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for j in range(E):
        u, v, w = graph[j]
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("O grafo contém um ciclo de peso negativo")
            return

    return dist

def result(nameFile, vert):
    graph_str = belmanReadTxt.read(nameFile)
    graph_list = graph_str.split(';')
    graph = []
    V = 0
    for line in graph_list:
        if line:
            node, edges = line.split(':')
            node = ord(node) - ord(vert)
            V = max(V, node)
            edges = edges.split(',')
            for edge in edges:
                v, w = edge.split('=')
                v = ord(v) - ord(vert)
                V = max(V, v)
                w = int(w)
                graph.append((node, v, w))
    V += 1
    E = len(graph)

    distances = bellman_ford(graph, V, E, 0)
    print(distances)
