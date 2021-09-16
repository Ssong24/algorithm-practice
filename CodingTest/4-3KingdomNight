# 4-1 상하좌우 문제와 비슷
# 말이 갈 수 있는 방향을 정의 (8가지)
# dx, dy
# 도착위치가 체스판 안이면 카운트 증가

def ChessNight(init):
  # 체스판 크기 설정
  chess_size = 8
  
  # 열과 행의 초기 위치 설정
  y = int(init[1]) - 1  # index 0,0 ~ 7,7
  x = ord(init[0]) - ord('a')
  
  answer = 0
  # 말이 갈 수 있는 방향 8가지 
  dx = [2,  2,-2, -2, 1, 1, -1, -1]
  dy = [1, -1, 1, -1, 2, -2, 2, -2]

  for i in range(len(dx)):
    nx = x + dx[i]
    ny = x + dy[i]
    # 도착 위치가 체스판 안이면 카운트 증가
    if 0 <= nx < chess_size and 0 <= ny < chess_size:
      answer += 1
  
  return answer

print(ChessNight('a1'))
