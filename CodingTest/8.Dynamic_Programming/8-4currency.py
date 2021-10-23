import time


def currency(m, coins):
    # Initialize DP table
    MAX = 10001
    count = [MAX] * (m + 1)

    # Omit the coin less than m
    coins = [coin for coin in coins if coin <= m]

    for coin in coins:
        count[coin] = 1
        # Bottom-Up DP
        for i in range(coin+1, m+1):
            count[i] = min(count[i], count[i-coin] + 1)

    answer = count[m]
    if answer == MAX:
        answer = -1
    return answer

n, m = 100, 10000  # map(int, input().split())

coins= [x for x in range(1, n+1)] 
print(coins)
# for i in range(n):
#     coins.append(int(input()))
start = time.time()
print(currency(m, coins))
end = time.time()
print("Time: {:5f}".format(end - start))  # limit: 1[sec]
