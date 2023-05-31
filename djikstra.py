import readTxt
def dijkstra(graph, start):
    distances = {u: float('inf') for u in graph}
    distances[start] = 0
    visited = set()
    while len(visited) < len(graph):
        u = min((u for u in graph if u not in visited), key=lambda u: distances[u])
        visited.add(u)
        for v_data in graph[u]:
            if '=' in v_data:
                v, weight = v_data.split('=')
                weight = int(weight)
            else:
                v = v_data
                weight = 1
            if distances[v] > distances[u] + weight:
                distances[v] = distances[u] + weight
    return distances

def result(nameTxt, raiz):
  graph = readTxt.readTxt(nameTxt)
  distances = dijkstra(graph, raiz)
  print(distances)
  
