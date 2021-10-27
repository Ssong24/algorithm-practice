# 예제 4-4 게임 개발 
# 여기서, 뒷 칸으로 갈 때 바다일 경우에 게임 종료이므로
# 방문한 곳과 바다인 곳의 정보를 구분해줘야 한다. 

def gameDev(size, posInfo, maze):
  n, m = map(int,size.split())  # 맵의 크기 
  x, y, d = map(int, posInfo.split()) # 캐릭터의 현재 위치, 방향
  
  # 맵의 정보 입력받기 - 바다/육지
  nMaze = []
  for i in range(n):
    nMaze.append(list(map(int,maze[i].split())))
  
  # 방문했는지 안했는 지. (바다 부분은 방문했다고 표시)
  visited = nMaze.copy()
  
  # 회전 방향 4가지에 따른 이동방향
  steps=[(-1,0), (0,1), (1,0), (0,-1)]

  # 현재 위치 방문 표시
  visited[x][y] = 1
  count = 1

  while True:
    # 회전 4방향 하기
    for i in range(len(steps)):
      d = (d - 1) % len(steps) # 반 시계방향으로 회전
      # 이동할 경우 좌표
      nx = x + steps[d][0]
      ny = y + steps[d][1]

      # 방문 안했고 바다 아닌 경우 이동
      if nMaze[nx][ny] == 0 and visited[nx][ny] == 0: 
        x, y = nx,ny
        visited[nx][ny] = 1
        count += 1
        break

    
    # 회전 4번 다 했을 경우
    if i == len(steps)-1:
      # 현재 방향에서 뒷 칸으로 이동할 경우 좌표
      nx, ny = x - steps[d][0], y - steps[d][1]

      if nMaze[nx][ny] == 1: # 뒷칸이 바다일경우
        break

      # 뒷 칸이 육지일 경우
      x, y = nx, ny
      if visited[nx][ny] == 0: # 뒷 칸이 육지인데, 방문 안했을 때
        visited[nx][ny] = 1
        count+= 1

  return count

size = "4 4"
posInfo = "1 1 0"
maze= ["1 1 1 1",
      "1 0 0 1",
      "1 1 0 1",
      "1 1 1 1"]

print(gameDev(size, posInfo, maze))
