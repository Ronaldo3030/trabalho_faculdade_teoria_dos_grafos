# import readTxt

# def BellmanFord(grafo, origem):
#     distancia = {}
#     predecessor = {}
#     for vertice in grafo:
#         distancia[vertice] = float('inf')
#         predecessor[vertice] = None
#     distancia[origem] = 0

#     for _ in range(len(grafo) - 1):
#         for vertice in grafo:
#             for vizinho in grafo[vertice]:
#                 if distancia[vizinho] > distancia[vertice] + grafo[vertice][vizinho]:
#                     distancia[vizinho] = distancia[vertice] + grafo[vertice][vizinho]
#                     predecessor[vizinho] = vertice

#     for vertice in grafo:
#         for vizinho in grafo[vertice]:
#             if distancia[vizinho] > distancia[vertice] + grafo[vertice][vizinho]:
#                 return None, None

#     return distancia, predecessor

# def result(nameTxt, raiz):
#   graph = readTxt.readTxt(nameTxt)
#   distancia, predecessor = BellmanFord(graph, 'S')
#   print(distancia)
#   print(predecessor)

def BellmanFord(grafo, origem):
    distancia = {}
    predecessor = {}
    for vertice in grafo:
        distancia[vertice] = float('inf')
        predecessor[vertice] = None
    distancia[origem] = 0

    for _ in range(len(grafo) - 1):
        for vertice in grafo:
            for vizinho in grafo[vertice]:
                if distancia[vizinho] > distancia[vertice] + grafo[vertice][vizinho]:
                    distancia[vizinho] = distancia[vertice] + grafo[vertice][vizinho]
                    predecessor[vizinho] = vertice

    for vertice in grafo:
        for vizinho in grafo[vertice]:
            if distancia[vizinho] > distancia[vertice] + grafo[vertice][vizinho]:
                return None, None

    return distancia, predecessor

grafo = {'A': {'B': 1, 'C': 4, 'D': 2, 'S': 5},
         'B': {'A': 1, 'C': 2, 'D': 3, 'S': 2},
         'C': {'A': 4, 'B': 2, 'D': 1},
         'D': {'A': 2, 'B': 3, 'C': 1, 'S': 3},
         'S': {'A': 5, 'B': 2, 'D': 3}}

distancia, predecessor = BellmanFord(grafo, 'S')
print(distancia)
print(predecessor)
