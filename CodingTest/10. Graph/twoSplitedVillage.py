# Find operation
def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

# Union operation
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def twoSplitedVillage():
    v, m = 7, 12  # map(int, input().split())
    parent = [0] * (v + 1)

    # List for necessary route s
    edges =[]
    # final cost
    result = 0

    # Initialize itself as parent node
    for i in range(1, v + 1):
        parent[i] = i

    # for _ in range(m):
    #     a, b, cost = map(int, input().split())
    #     # To sort by cost, set cost as first element of tuple
    #     edges.append((cost, a, b))

    edges.append((3, 1, 2))
    edges.append((2, 1, 3))
    edges.append((1, 3, 2))
    edges.append((2, 2, 5))
    edges.append((4, 3, 4))
    edges.append((6, 7, 3))
    edges.append((5, 5, 1))
    edges.append((2, 1, 6))
    edges.append((1, 6, 4))
    edges.append((3, 6, 5))
    edges.append((3, 4, 5))
    edges.append((4, 6, 7))

    edges.sort()
    # last maximum cost of necessary routes
    last = 0

    for edge in edges:
        cost, a, b = edge

        # if no cycle, union
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)

            result += cost
            last = cost

    print(result-last)


twoSplitedVillage()
