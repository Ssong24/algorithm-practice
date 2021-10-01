def swap():
  # 입력 받기
  n, k= map(int, input().split())
  arrA = list(map(int, input().split()))
  arrB = list(map(int, input().split()))
  
  # 오름차순 정렬
  arrA.sort()
  arrB.sort()

  # 배열 A의 제일 작은 수 k번째까지와
  # 배열 B의 제일 큰 수 k번째까지와 교체
  arrA[:k], arrB[-k:] = arrB[-k:], arrA[:k]

  print(sum(arrA))

swap()
