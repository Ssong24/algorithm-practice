import heapq
INF = int(1e9)

def dijkstra(graph, start, distance):
    q = []
    heapq.heappush(q, (0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


def futureCity(start, k, x, graph, distance):
    dijkstra(graph, start, distance)
    start2k = distance[k]
    dijkstra(graph, k, distance)
    k2x = distance[x]
    answer = start2k + k2x
    if answer >= INF:
        return -1
    else:
        return answer

n,m = map(int, input().split())  # 노드, 간선 (1 ~ 100)  # 5, 7
graph = [[] for _ in range(n+1)]  # 그래프 정보
for _ in range(m):  # 간선 정보 입력받기
    a, b = map(int, input().split())
    graph[a].append([b,1])
    graph[b].append([a,1])

x, k = map(int, input().split())  # 1 ~ 100 4, 5 map(int, input().split())  # 1 ~ 100

distance = [INF] * (n+1)
start = 1
print(futureCity(start,k,x, graph, distance))



"""
입력 예시 1)
n, m = 5, 7
# graph[1].append([2,1])
# graph[1].append([3,1])
# graph[1].append([4,1])
#
# graph[2].append([1,1])
# graph[2].append([4,1])
#
# graph[3].append([1,1])
# graph[3].append([4,1])
# graph[3].append([5,1])
#
# graph[4].append([1,1])
# graph[4].append([2,1])
# graph[4].append([3,1])
# graph[4].append([5,1])
#
# graph[5].append([3,1])
# graph[5].append([4,1])
x, k = 4, 5
출력: 3

입력 예시 2)
n, m = 4,2
graph[1].append([3,1])
graph[2].append([4,1])
graph[3].append([1,1])
graph[4].append([2,1])
x,k = 3, 4
출력: -1
"""
