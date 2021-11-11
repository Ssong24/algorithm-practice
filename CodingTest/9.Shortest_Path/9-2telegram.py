"""
다익스트라 / 플로이드 워셜 (FW)
노드 갯수, 간선 갯수
경로 정보 담는 그래프 (FW: cost 담음)
최초 지점과의 거리 정보 담는 리스트(다익스트라)
자료구조: 최소 힙
"""
import heapq as hq
import sys
input = sys.stdin.readline
INF = int(1E+9)

v, e, start = map(int, input().split())  # 5, 3, 1
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])  # 이웃노드, 비용


def dijkstra(start, graph, distance):
    h = []
    distance[start] = 0
    hq.heappush(h, (0, start))

    while h:
        nowCost, now = hq.heappop(h)
        for i in graph[now]:
            next, nextCost = i[0], i[1]
            allCost = nowCost + nextCost
            if allCost < distance[next]:
                distance[next] = allCost
                hq.heappush(h, (allCost, next))


def telegram(start, graph, distance):
    dijkstra(start, graph, distance)
    answer = 0
    n_city = 0
    for d in distance:
        if d != INF:
            answer = max(answer, d)
            n_city += 1

    answer -= 1  # start 노드 빼주기
    print(n_city, answer)

telegram(start, graph, distance)


# 그래프 input
# graph[1].append([2,1])
# graph[1].append([3,2])
# graph[1].append([5,1])
# graph[2].append([4,3])
# graph[4].append([5,1])
# ouput
# 4 4
