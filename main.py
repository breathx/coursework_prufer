cases = ['0', '1', 'code', 'decode']

while True:
    choice = input('Please, choose the menu point:\n\
~ Prufer code (> 0 or > code)\n\
~ Prufer decode (> 1 or > decode)\n\
> ')
    print()
    if choice in cases:
        break

if choice in ['0', 'code']:
    print('Please, enter the edges of the graph separated \
by a space, one in each line.\n\
To stop typing, enter an empty string:')

    n = 0
    edges = {}

    edge_input = input('> ')
    while edge_input != '':
        edge_input = [int(i) - 1 for i in edge_input.split()]

        n = max(n, max(edge_input[0], edge_input[1]) + 1)

        if edge_input[0] in edges:
            edges[edge_input[0]] += [edge_input[1]]
        else:
            edges[edge_input[0]] = [edge_input[1]]
        
        if edge_input[1] in edges:
            edges[edge_input[1]] += [edge_input[0]]
        else:
            edges[edge_input[1]] = [edge_input[0]]
        
        edge_input = input('> ')

    degrees = [0] * n
    leaves = []

    for i in range(n):
        degree = len(edges[i])
        degrees[i] = degree
        if degree == 1:
            leaves += [i]

    prufer_code = []
    cut = [False] * n

    for _ in range(n - 2):
        leaves.sort(reverse=True)
        leaf = leaves.pop()
        cut[leaf] = True

        for vertex in edges[leaf]:
            if not cut[vertex]:
                parent = vertex
        
        prufer_code += [parent + 1]
        degrees[parent] -= 1
        if degrees[parent] == 1:
            leaves += [parent]

    print('\nPrufer code for your graph:')
    print(*prufer_code)
else:
    prufer_code = [int(i) - 1 for i in input(
        'Please, enter prufer code for you graph:\n').split()]

    n = len(prufer_code) + 2

    degrees = [1] * n

    for vertex in prufer_code:
        degrees[vertex] += 1

    leaves = []
    for vertex in range(n):
        if degrees[vertex] == 1:
            leaves += [vertex]

    edges = {}
    for vertex in range(n):
        edges[vertex] = []

    for vertex in prufer_code:
        leaves.sort(reverse=True)
        leaf = leaves.pop()

        edges[leaf] += [vertex]
        edges[vertex] += [leaf]

        degrees[vertex] -= 1
        if degrees[vertex] == 1:
            leaves += [vertex]

    edges[leaves[0]] += [leaves[1]]
    edges[leaves[1]] += [leaves[0]]

    print('\nEdges of your graph:')
    for vertex in range(n):
        for neighbour in edges[vertex]:
            if neighbour > vertex:
                print(f'> {(vertex + 1):>2d} {(neighbour + 1):<2d}')
