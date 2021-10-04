""" 두 배열(A,B)의 원소 교체해서 배열 A의 원소 합이 최대가 되도록
N k: 배열 크기, 교체 횟수
배열 A의 원소들
배열 B의 원소들
입력 예시:
 5 3
 1 2 5 4 3
 5 5 6 6 5
"""
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
