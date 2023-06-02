import simpleReadTxt
def posOrdem(tree, node, visited=None):
    if visited is None:
        visited = set()
    if node in visited:
        return []
    visited.add(node)
    result = []
    if node in tree:
        for child in tree[node]:
            result.extend(posOrdem(tree, child, visited))
    result.append(node)
    return result

def result(nameTxt, raiz):
    try:
        tree_str = simpleReadTxt.read(nameTxt)
        tree = {}
        for line in tree_str.split(';'):
            if line:
                node, children = line.split(':')
                tree[node] = children.split(',')
        result = posOrdem(tree, raiz)
        print(result)
    except:
        print("Erro: Arquivo não encontrado")
  

