def UntilOne(N_K):
  # N, K을 공백으로 구분하여 입력받기
  N, K = map(int, N_K.split())

  answer = 0
  while N != 1:
    if N % K != 0: # 나누어 떨어지지 않을 때 
      # 나머지 만큼 answer에 바로 더해주고 N 업데이트   
      answer += N % K 
      N -= N % K
    else:
      answer += 1
      N = N // K
  
  
  return answer


N_K = "17 4" # "25 5"
print(UntilOne(N_K))
