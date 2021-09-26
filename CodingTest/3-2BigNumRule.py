# 큰수의 법칙
# 가장 큰 수와 2번째로 큰 수 뽑기.

def solution(M, K, num_list):
  max1, max2 = 0, 0
  answer  = 0
  
  # 내림차순으로 정렬
  num_list.reverse()

  # 가장 큰 수, 두번째로 큰 수 저장
  max1, max2 = num_list[0], num_list[2]
  
  # 방법2: M 갯수 만큼 더하기
  for i in range(0,M):
      if i % K != 0 or i == 0: # index 0 ~ k-1 까진 큰 수 더하기 
        answer += max1
      else: # index K 배수 때마다 두번째로 큰 수 더하기
        answer += max2
  #print(answer)

  # 방법2: 반복되는 수열 이용  **
  answer2 = 0
  unit_sum = K * max1 + max2
  quotient = M // (K+1)
  remainder = M % (K+1)
  answer2 = unit_sum * quotient + remainder * max1

  #print(answer2)

  return answer


N,M,K = 5, 8, 3
num_list = [2,4,5,4,6]
    
print(solution(M,K, num_list))
