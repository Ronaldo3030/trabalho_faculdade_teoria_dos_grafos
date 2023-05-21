import readTxt

def preOrdem(graph, node, visited=None):
    if visited is None:
        visited = []
    result = [node]
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            result.extend(preOrdem(graph, neighbor, visited))
    return result

def result(nameTxt, node):
  graph = readTxt.readTxt(nameTxt)
  result = preOrdem(graph, node)
  print(result)
