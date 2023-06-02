def read(filename):
    try:
        with open(filename, 'r') as f:
            graph_str = f.read().replace('\n', '')
        graph = {}
        for line in graph_str.split(';'):
            if line:
                node, children = line.split(':')
                graph[node] = children.split(',')
        return graph
    except:
        print("Erro: Arquivo não encontrado")