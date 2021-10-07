# 7-2 Tteokbokki
# Get N number of ricecakes and requested the length M
# Solve highest length of ricecake H
def tteokbokki():
  n, m = map(int, input().split())
  tteoks = list(map(int, input().split()))
  # Initialize start and end length
  start, end = 0, max(tteoks)
  
  while start <= end:
    mid = (start + end) // 2
    total = 0
    
    # Calculate ricecakes' length after cut
    for x in tteoks:
      if x > mid:
        total += x - mid
    if total == m:
      return mid
    elif total > m:
      start = mid + 1
    elif total < m:
      end = mid - 1
  return False

print(tteokbokki())
