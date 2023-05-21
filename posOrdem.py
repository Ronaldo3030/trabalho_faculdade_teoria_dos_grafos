import readTxt
def posOrdem(graph, node, visited=None):
    if visited is None:
        visited = []
    result = []
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            result.extend(posOrdem(graph, neighbor, visited))
    result.append(node)
    return result

def result(nameTxt, node):
  graph = readTxt.readTxt(nameTxt)
  result = posOrdem(graph, node)
  print(result)
  

