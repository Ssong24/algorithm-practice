import time


def floorConstruct(n):
    answer = [0] * (n+1)
    answer[1] = 1
    answer[2] = 3

    for i in range(3, n+1):
        answer[i] = answer[i-2] * 2 + answer[i-1]

    return answer[n] % 796796


n = int(input())  # 1~1000
start = time.time()
result = floorConstruct(n)
end = time.time()
print(result)
print('Time: {:5f}'.format(end-start))  # linmit: 1[sec]
