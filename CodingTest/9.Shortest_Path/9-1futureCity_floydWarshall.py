INF = int(1e9)

# Get number of nodes and edges
n, m = map(int, input().split())
# Initialize graph value to INF
graph = [[INF] * (n+1) for _ in range(n+1)]

# Set graph value to one when going to itself
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# Get edge info, and initialize
for _ in range(m):
    # Set cost as one from a to b
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# Get input of pass-by node X and final point K
x, k = map(int, input().split())

# By recurrence relation, run Floyd Warshall algorithm
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])

# Display the answer
distance = graph[1][k] + graph[k][x]

# If unreachable, print -1
if distance >= INF:
    print("-1")
# If reachable, print shortest distance
else:
    print(distance)
