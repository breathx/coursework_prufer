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