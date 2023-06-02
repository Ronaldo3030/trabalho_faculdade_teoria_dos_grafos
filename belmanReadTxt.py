def read(filename):
    with open(filename, 'r') as f:
        graph_str = f.read()
    graph_str = graph_str.replace(';\n', ';')
    return graph_str
