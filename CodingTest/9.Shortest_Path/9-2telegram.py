import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m, start = 5,3, 1 # map(int, input().split())
# Initialize Graph (edge info)
graph = [[] for _ in range(n+1)]
# Initialize distance (start to specific node)
distance = [INF] * (n+1)

graph[1].append([2,1])
graph[1].append([3,2])
graph[1].append([5,1])
graph[2].append([4,3])
graph[4].append([5,1])
# Get input of graph info
# for _ in range(m):
#     a, b, cost = map(int, input().split())
#     graph[a].append([a, b])  # 이웃 노드, 비용

def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    count, time = 0, 0
    for i in range(1, n+1):
        if distance[i] != INF:
            count += 1
            if time < distance[i]:
                time = distance[i]
    count -= 1  # start 노드 빼주기

    return count, time

count, time = dijkstra(start, graph, distance)
print(count, time)  # 4, 4
