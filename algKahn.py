import kahnReadTxt


def kahn_topological_sort(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = []
    for u in in_degree:
        if in_degree[u] == 0:
            queue.insert(0, u)

    result = []
    while queue:
        u = queue.pop()
        result.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.insert(0, v)

    if len(result) != len(graph):
        return None
    return result


def result(nameTxt):
    try:
        graph = kahnReadTxt.read(nameTxt)
        result = kahn_topological_sort(graph)
        print(result)
    except FoundError:
        print("Erro: Arquivo não encontrado")
