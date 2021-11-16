# 위상 정렬

from collections import deque
import copy

v = int(input())
time = [0] * (v+1)  # 각 강의 시간을 0으로 초기화
indegree = [0] * (v+1)  # 모든 노드의 진입차수 0으로 초기화
graph = [[] for i in range(v+1)]  # 각 노드에 연결된 간선 정보

for a in range(1, v+1):
    infoVer = list(map(int, input().split()))
    time[a] = infoVer[0]  # 각 노드의 강의시간

    for b in infoVer[1:-1]:  # 각 노드의 간선들 리스트: 강의시간과 맨 끝 -1을 제외한 부분
        graph[b].append(a)
        indegree[a] += 1


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    answer = 0


    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    answer = time[q[0]]

    while q:
        now = q.popleft()
        maxTime = 0

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                maxTime = max(maxTime, time[i])
                q.append(i)
                result[i] += result[now]
        answer += maxTime

    for i in range(1, v+1):
        print(result[i])

    return answer

print('Total time: ', topology_sort())
