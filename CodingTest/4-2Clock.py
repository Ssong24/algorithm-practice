# 예제 4-2 시각
# 0시 0분 0초에서 N시 59분 59초까지 
# 완전 탐색으로 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수 출력

def clock(N):
  h = N
  count = 0
  
  for i in range(h+1):
    for j in range(60):
      for k in range(60):
        # 매 시각마다 '3'이 포함되면 count 증가
        if '3' in str(i) + str(j) + str(k):
          count+= 1
  return count 

N = 5
print(clock(N))
