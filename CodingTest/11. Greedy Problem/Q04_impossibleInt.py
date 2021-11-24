import random, time

# 만들 수 없는 금액
def impossibleInt(coins):
    coins.sort()  # 오름차순으로 정렬
    target = 1

    for x in coins:
        if target < x:
            break
        target += x

    # 만들 수 없는 금액 리턴
    return target


N = 1000  # int(input())  # number of coins  1 <= N <= 1000
coins = []  # list(map(int, input().split()))  # 1 <= coin <= 1000000
for _ in range(N):
    coins.append(random.randint(1, 100))  # 계산 증가를 위해 100으로 범위 낮춤

start_t = time.time()
print(impossibleInt(coins))
end_t = time.time()
print('Time:{:.4f}'.format(end_t - start_t))

# 출력: 51669
# Time:0.0000
