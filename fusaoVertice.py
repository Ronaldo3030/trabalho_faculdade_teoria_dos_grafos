import readTxt
import convertInput


def fusaoVertice(graph, v1, v2):
    if v1 not in graph or v2 not in graph:
        return "Um ou ambos os vértices não estão presentes no grafo"

    new_vertex = v1 + v2

    graph[new_vertex] = set()

    for neighbor in graph[v1]:
        if neighbor != v2:
            graph[new_vertex].add(neighbor)
            graph[neighbor].add(new_vertex)

    for neighbor in graph[v2]:
        if neighbor != v1:
            graph[new_vertex].add(neighbor)
            graph[neighbor].add(new_vertex)

    del graph[v1]
    del graph[v2]

    for vertex in graph:
        if v1 in graph[vertex]:
            graph[vertex].remove(v1)
        if v2 in graph[vertex]:
            graph[vertex].remove(v2)

    return graph


def result(nameTxt, v1, v2):
    try:
        input_str = readTxt.readTxt(nameTxt)
        graph = convertInput.convert_input_to_set(input_str)
        new_graph = fusaoVertice(graph, v1, v2)
        print(new_graph)
    except:
        print("Erro: Arquivo não encontrado")
