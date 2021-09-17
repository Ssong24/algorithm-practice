# 예제 5-3 음료수 얼려먹기
# DFS로 가능
# 이 문제에서는 칸막이 존재하는 부분(1)은 가지 못하므로 방문한 곳으로 가정한다. 
def dfs(graph, x,y):
  # 상,하,좌,우 방향
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  # 현재 위치 방문 표시
  graph[x][y] = 1

  for i in range(len(dx)): # 4개 방향 모두 체크
    nx = x + dx[i]
    ny = y + dy[i]
    # 그래프 영역 안이고 방문하지 않은 곳이면 dfs 호출
    if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] != 1:
        dfs(graph, nx,ny)
  return 1

def freezeCan(size, matrix):
  # 그래프 크기
  n, m = map(int, size.split())
  
  # 그래프 정보 입력받기
  new_matrix = []
  for i in range(n):
    new_matrix.append(list(map(int, matrix[i].split())))

  answer = 0
  for i in range(n):
    for j in range(m):
      if new_matrix[i][j] == 0:  # 방문하지 않은 곳이면 dfs 호출
        answer += dfs(new_matrix, i,j)
  return answer

size = "15 14"
matrix = ["0 0 0 0 0 1 1 1 1 0 0 0 0 0 ",
          "1 1 1 1 1 1 0 1 1 1 1 1 1 0 ",
          "1 1 0 1 1 1 0 1 1 0 1 1 1 0 ",
          "1 1 0 1 1 1 0 1 1 0 0 0 0 0 ",
          "1 1 0 1 1 1 1 1 1 1 1 1 1 1 ",
          "1 1 0 1 1 1 1 1 1 1 1 1 0 0 ", 
          "1 1 0 0 0 0 0 0 0 1 1 1 1 1 ",
          "0 1 1 1 1 1 1 1 1 1 1 1 1 1 ",
          "0 0 0 0 0 0 0 0 0 1 1 1 1 1 ", 
          "0 1 1 1 1 1 1 1 1 1 1 0 0 0 ",
          "0 0 0 1 1 1 1 1 1 1 1 0 0 0 ", 
          "0 0 0 0 0 0 0 1 1 1 1 0 0 0 ",
          "1 1 1 1 1 1 1 1 1 1 0 0 1 1 ",
          "1 1 1 0 0 0 1 1 1 1 1 1 1 1 ", 
          "1 1 1 0 0 0 1 1 1 1 1 1 1 1 "
          ]

print(freezeCan(size, matrix))
