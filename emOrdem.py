import simpleReadTxt
def emOrdem(tree, node, visited=None):
    if visited is None:
        visited = set()
    if node in visited:
        return []
    visited.add(node)
    result = []
    if node in tree:
        children = tree[node]
        result.extend(emOrdem(tree, children[0], visited))
        result.append(node)
        for child in children[1:]:
            result.extend(emOrdem(tree, child, visited))
    else:
        result.append(node)
    return result

def result(nameTxt, raiz):
    tree_str = simpleReadTxt.read(nameTxt)
    tree = {}
    for line in tree_str.split(';'):
        if line:
            node, children = line.split(':')
            tree[node] = children.split(',')
    result = emOrdem(tree, raiz)
    print(result)