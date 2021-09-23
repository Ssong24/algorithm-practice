from collections import deque

def bfs(maze, initPos, visited):
  x, y = initPos[0]-1, initPos[1]-1 # 출발지
  n, m = len(maze), len(maze[0]) # 미로의 크기

  # 큐 구현을 위해 deque 라이브러리 사용
  queue = deque([(x,y)])
  # 현재 노드 방문 처리
  visited[x][y] = True
  # 이동방향 4가지
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  
  while queue:    
    x, y= queue.popleft()
    
    for i in range(len(dx)):
      nx, ny = x + dx[i], y + dy[i]
      
      if 0 <= nx < n and 0 <= ny < m:  # 지도 안에 있을 때
        if maze[nx][ny] != 0 and not visited[nx][ny]: # 괴물이 없고, 방문한 곳이 아닐경우
          queue.append((nx, ny))
          visited[nx][ny] = True
          maze[nx][ny] = maze[x][y] +1
          

def mazeEscape(maze,size):
  # 입력받기
  n,m = map(int, size.split())
  nMaze, visited = [], []
  
  for i in range(n):
    nMaze.append(list(map(int, maze[i])))
    visited.append([False]*m)
  
  bfs(nMaze, (1,1), visited)
  
  return nMaze[n-1][m-1]

size = "5 6"
maze = ["101010",
        "111111",
        "000001",
        "111111",
        "111111"]

print(mazeEscape(maze, size))
