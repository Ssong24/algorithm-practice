# 바닥 공사
# (width, height) = (n,2) tile
# With 1x2, 2x1, 2x2, find case number 
# a_i = a_(i-1) + a_(i-2) * 2
def floorConstruct(n):
    # Initialize DP table
    d = [0] * (n+1)
    
    # Bottom-Up DP
    d[1] = 1  # 2x1 일때 경우의 수
    d[2] = 3
    for i in range(3, n+1):
        d[i] = (d[i-1] + 2 * d[i-2]) % 796796

    print(d[n])

# Input:5
# Output: 21 
floorConstruct(5)
