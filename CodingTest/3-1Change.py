# 거스름돈 문제
# 카운터에서 사용 가능한 거스름돈: 500,100,50,10원 
# 손님에게 줘야할 돈 N원일때, 최소 동전 갯수로 거슬러 주는 방법은?
# (단, 거스러 줘야 할 돈은 항상 10의 배수)

# Point! 가장 큰 화폐부터 거슬러 주기

def solution(N):
  coin_types = [500,100,50,10] # 이름 명시 명확히
  answer = 0
  
  for coin in coin_types:   
    #num = int(N / coin)  
    #N -= coin*num
    answer += n // coin 
    N %= coin # N은 coin으로 나눌 때 나머지를 바로 업데이트 해주면 된다.

  return answer
    
solution(1260)
