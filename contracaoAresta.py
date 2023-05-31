import readTxt
import convertInput
def contract_edge(graph, edge):
    u, v = edge
    if u not in graph or v not in graph:
        return
    for w in graph[v]:
        if w != u:
            graph[u].append(w)
            graph[w].remove(v)
            graph[w].append(u)
    del graph[v]
    graph[u] = list(set(graph[u]))

def result(nameTxt, v1, v2):
  graph = readTxt.readTxt(nameTxt)
  contract_edge(graph, (v1, v2))
  print(graph)