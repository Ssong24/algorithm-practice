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


def team_formation():
    v, m = map(int, input().split())
    parent = [0] * (v + 1)

    # Initialize itself as parent node
    for i in range(1, v + 1):
        parent[i] = i

    for _ in range(m):
        oper, a, b = map(int, input().split())

        if oper == 0:  # 합집합(union) 연산
            union_parent(parent, a, b)
        elif oper == 1:  # 찾기(find) 연산
            if find_parent(parent, a) != find_parent(parent, b):
                print("NO")
            else:
                print("YES")

team_formation()
