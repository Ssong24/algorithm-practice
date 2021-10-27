# Card Game
def CardGame(NM, matrix):
  # N, M을 공백으로 구분하여 입력받기
  N, M = map(int, NM.split())

  answer = 0
  
  for row in range(N):
    # 배열 형태의 matrix
    matrix[row].sort() # 각 행에서 가장 작은 수 찾기
    
    # data = list(map(int, input().split())) # 한 줄 씩 입력받기

    if matrix[row][0] > answer: # 0번째 열에서 가장 큰 수 찾기
      answer = matrix[row][0]
  
  return answer


NM = "2 4"
matrix = [[7,3,1,8],[3,3,3,4]]
CardGame(NM, matrix)
    
