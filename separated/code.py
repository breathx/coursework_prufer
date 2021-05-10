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
