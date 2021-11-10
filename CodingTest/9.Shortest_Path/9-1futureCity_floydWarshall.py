import heapq as hq
# 다익스트라 / 플로이드 워셜 (FW)
"""
노드 갯수, 간선 갯수
경로 정보 담는 그래프 (FW: cost 담음)
최초 지점과의 거리 정보 담는 리스트(다익스트라)
자료구조: 최소 힙
"""

INF = int(1E+9)


def floyd_warshall(v, graph):
    for i in range(1, v+1):
        for j in range(1, v+1):
            for l in range(1, v+1):
                graph[i][j] = min(graph[i][j], graph[i][l] + graph[l][j])


def future_city(v, x, k, graph):
    # By recurrence relation, run Floyd Warshall algorithm
    floyd_warshall(v, graph)

    # save the shortest distance
    result = graph[1][k] + graph[k][x]

    # Display the answer
    if result < INF:
        print(result)
    else:
        print(-1)


if __name__ == '__main__':
    # Get number of nodes and edges
    v, e = map(int, input().split())
    # 그래프 초기화 하는 방법 **
    graph = [[INF] * (v+1) for _ in range(v + 1)]  # 노드에 따라 연결 정보 있기 때문에 노드 갯수 만큼 만들어줌 (+1은 인덱스 바로 적용을 위함)

    # 자기 자신으로 가는 비용은 0으로 초기화 ***
    for a in range(1, v+1):
        for b in range(1, v+1):
            if a == b:
                graph[a][b] = 0

    # Each edge info
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1

    # Get input of pass-by node k and final point node x
    x, k = map(int, input().split())

    future_city(v, x, k, graph)
