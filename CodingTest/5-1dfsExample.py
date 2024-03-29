# DFS 예제 
# 스택 자료구조에 기초
# 1. 탐색 시작 노드를 스택에 삽입 후 방문처리 
# 2-1. 최상단 노드에 방문하지 않은 인접노드가 있으면 그 인접 노드 넣고 방문 처리
# 2-2. 인접 노드 모드 방문 시 스택에서 최상단 노드 꺼내기
# 3. 2번 과정을 더 이상 수행X 까지 반복
# 실행시간: O(N)
def dfs(graph, v, visited):
  # 현재 노드 방문 처리
  visited[v] = True
  print(v, end=' ')

  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

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

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
