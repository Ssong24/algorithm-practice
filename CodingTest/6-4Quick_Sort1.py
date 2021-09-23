# 예제 6-4 퀵 정렬
# 맨 앞 원소를 pivot 설정
# pivot 뒷 기준으로 맨 왼쪽과 맨 오른쪽 원소 위치에서 시작해서
# 왼쪽에서는 pivot 보다 큰 데이터, 오른쪽에서는 더 작은 데이터를 뽑아
# swap 한다. 
# left와 right 위치가 엇갈리면 더 작은 데이터와 pivot 데이터를 교환 
def quick_sort(array, start, end): 
  print(array)
  # start, end 는 인덱스
  if start >= end: # 원소가 1개일 경우 종료
    return
  pivot = start # 피벗은 첫번째 원소

  left = start + 1
  right = end

  while left <= right:
    # left 인덱스가 end 인덱스보다 이하이고, 피벗보다 큰 데이터 찾을 때까지 반복
    while left <= end and array[left] <= array[pivot]:
      left += 1
    
    # right 인덱스가 start 인덱스 초과이고, 피벗보다 작은 데이터 찾을 때까지 반복
    while right > start and array[right] >= array[pivot]:
      right -= 1
    # 인덱스가 엇갈리면 작은 데이터와 피벗을 교체
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
      array[left], array[right] = array[right], array[left]
  
  # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
  quick_sort(array, start, right-1)
  quick_sort(array,right+1, end)

  

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(array, 0, len(array)-1)
