def convert_input_to_set(input_dict):
    graph = {}
    for vertex, neighbors in input_dict.items():
        graph[vertex] = set(neighbors)
    return graph