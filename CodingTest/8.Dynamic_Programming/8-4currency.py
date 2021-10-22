# 효율적인 화폐 구성
def currency(m, coins):
    matrix = [10001] * (m+1)
    matrix[0] = 0
    coins.sort()

    init_point = coins[0]
    for k in coins:
        for i in range(init_point, m+1):
            matrix[i] = min(matrix[i], matrix[i-k] + 1)

    if matrix[m] != 10001:
        return matrix[i]
    else:
        return -1

# Get input
# n, m = map(int, input().split())
# coins = []
# for i in range(n):
#     coins.append(int(input()))
answer = currency(4, [3,5,7])
print(answer) # -1
