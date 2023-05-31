def pre_order(tree, node, visited=None):
    if visited is None:
        visited = set()
    if node in visited:
        return []
    visited.add(node)
    result = [node]
    if node in tree:
        for child in tree[node]:
            result.extend(pre_order(tree, child, visited))
    return result

tree_str = '50:40,60;40:30,45,50;60:55,70,50;30:40;45:40;55:60;70:60;'
tree = {}
for line in tree_str.split(';'):
    if line:
        node, children = line.split(':')
        tree[node] = children.split(',')

result = pre_order(tree, '50')
print(result)
