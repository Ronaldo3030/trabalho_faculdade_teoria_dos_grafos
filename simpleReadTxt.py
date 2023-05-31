def read(filename):
    with open(filename, 'r') as f:
        tree_str = f.read().replace('\n', '')
    return tree_str
