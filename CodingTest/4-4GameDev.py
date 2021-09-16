# 예제 4-4 시뮬레이션 문제
# 회전 방향, 이동방향 모두 정의
# 맵의 방문한 곳인지 아닌지 정보 저장
# 모든 방향 방문하면 뒤로 1칸
# 모든 방향 방문했는데, 뒤 1칸이 바다면 게임 Stop
import numpy as np
def DevelopGame(matrix_size, init_pos, mapInfo):
  N, M = map(int, matrix_size.split())
  x, y, d = map(int, init_pos.split())
  
  # 맵 정보 선언
  new_matrix = np.zeros((N,M))
  for i in range(N):
    new_matrix[i] = mapInfo[i].split()


  # 방문한 곳인지 체크
  visited = np.zeros((N,M))
  visited[x][y] = 1
  answer = 1

  # 회전 방향 4가지
  rot = [0,1,2,3]
  # 이동방향 4가지 (회전방향과 sync)
  steps = [(0,-1), (1,0), (0,1), (-1,0)]


  while True:
    i = 0
    for i in range(len(rot)):
      # 현 방향에서 왼쪽
      nd = d - 1 if d != 0 else len(rot) -1
      nx = x + steps[nd][0]
      ny = y + steps[nd][1]

      if visited[nx][ny] == 0 and new_matrix[nx][ny] == 0:
        x, y = nx, ny
        d = nd
        visited[x][y] = 1
        answer += 1
        continue
      elif new_matrix[nx][ny] == 1: # 왼쪽에 있는 칸이 바다일 때 break
        d = nd        
    
    # 4가지 방향으로 회전했을 때
    if i == len(rot)-1:
      # 뒷 칸이 바다가 아닐 때 뒤로 한 칸 이동
      if new_matrix[nx][ny] == 0:
        nx = x - steps[nd][0]
        ny = y - steps[nd][1]
        visited[nx][ny] = 1
        x, y = nx, ny  
        answer += 1
        continue  # 좌표 이동 후 1단계로 되돌아가기
      
      else:  # 뒷 칸이 바다일 때 게임 종료
          break    

  return answer


matrix_size = "4 4"
init_pos = "1 1 0"
mapInfo = ["1 1 1 1", "1 0 0 1", "1 1 0 1", "1 1 1 1"]
print(DevelopGame(matrix_size, init_pos, mapInfo))

