def top2bottom():
  # 입력 받기
  n = int(input())
  array = []
  for i in range(n):
    array.append(int(input()))
  
  # 삽입 정렬
  for i in range(0,n):
    for j in range(i,0,-1):
      if (array[j] > array[j-1]):
        array[j], array[j-1] = array[j-1], array[j]
      else:
        break
  return array

print(top2bottom())
