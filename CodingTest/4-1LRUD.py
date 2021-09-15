# 예제 4-1 상하좌우
# NxN 정사각형 공간에서 상하좌우로 움직이면서 좌표 이동
# 공간을 벗어나는 움직임은 무시
# 연산 횟수는 이동 횟수에 비례
def LRUD(N, route):
  # 입력 받기
  N = int(N)
  route =  route.split()

  answer = [0,0] 

  # L, R, U,D에 따른 이동방향
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]
  move_types = ['L', 'R', 'U', 'D']
  
  # 움직일 수 있는 공간 (0,0) ~ (N-1, N-1)
  for r in route:
    for i in range(len(move_types)):
      if r == move_types[i]:
        nx = answer[0] + dx[i]
        ny = answer[1] + dy[i]
        
    # 0보다는 이상, N-1 보다는 이하
    if nx < 0  or ny < 0 or nx > N-1 or ny > N-1:
      continue
    # 좌표 이동
    answer[0] = nx
    answer[1] = ny
    
  return answer


N = "5"
route = "R R R U D D"
result = LRUD(N,route)
print(result[0]+1,result[1] + 1)
    
