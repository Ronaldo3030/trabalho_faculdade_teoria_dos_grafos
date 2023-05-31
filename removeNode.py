import simpleReadTxt

def removeNode(tree, node):
    if node in tree:
        del tree[node]
    for parent, children in tree.items():
        if node in children:
            children.remove(node)
            
def result(nameTxt, raiz):
    tree_str = simpleReadTxt.read(nameTxt)
    tree = {}
    for line in tree_str.split(';'):
        if line:
            node, children = line.split(':')
            tree[node] = children.split(',')
    removeNode(tree, raiz)
    tree_str = ';'.join(f'{node}:{",".join(children)}' for node, children in tree.items())
    print(tree_str)