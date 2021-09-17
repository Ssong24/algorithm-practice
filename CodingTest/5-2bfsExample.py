# BFS 예제 
# 큐 자료구조에 기초
# 1. 탐색 시작 노드를 큐에 삽입 후 방문처리 
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중 방문X 노드를 모두 큐에 삽입 후 방문처리

# 3. 2번 과정을 더 이상 수행X 까지 반복
# 실행시간: O(N)

from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
  # Queue 구현을 위해 deque 라이브러리 사용
  queue = deque([start])
  # 현재 노드 방문 처리
  visited[start] = True
  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end= ' ')
    # 해당 원소의 인접 노드 중 방문 X 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True



# 각 노드가 연결된 정보를
# 리스트 자료형으로 표현 (2차원 리스트)
graph = [
  [],  # 노드 0 없지만, 인덱스 접근 쉽도록 공간을 만들기
  [2,3,8], # 노드 1에 연결된 노드들
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9 # 0 ~ 8

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

