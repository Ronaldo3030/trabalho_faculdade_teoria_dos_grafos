import simpleReadTxt

def preOrdem(tree, node, visited=None):
    if visited is None:
        visited = set()
    if node in visited:
        return []
    visited.add(node)
    result = [node]
    if node in tree:
        for child in tree[node]:
            result.extend(preOrdem(tree, child, visited))
    return result

def result(nameTxt, raiz):
    try:
        tree_str = simpleReadTxt.read(nameTxt)
        tree = {}
        for line in tree_str.split(';'):
            if line:
                node, children = line.split(':')
                tree[node] = children.split(',')
        result = preOrdem(tree, raiz)
        print(result)
    except:
        print("Erro: Arquivo não encontrado")