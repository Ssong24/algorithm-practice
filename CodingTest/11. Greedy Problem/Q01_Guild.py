from collections import Counter
import random
import time

def adventureGuild(fear):
    answer = 0
    fear = Counter(fear)
    pre = 0

    for k,v in fear.items():
        if v >= k:
            answer += v // k
            pre += v % k
        else:
            preSum = pre+v
            if preSum >= k:
                answer += preSum // k
                pre = preSum % k
    return answer

n = 100000   # int(input())
fear = []
for i in range(n):
    fear.append(random.randint(1, 5))    # 계산량을 증가했을 때 시간 체크하기 위해 randint(1,5)으로 설정.  원래는 randint(1, n)

# for _ in range(n):
#     fear = list(map(int, input()))

start_t = time.time()
print(adventureGuild(fear))
end_t = time.time()
print("{:.4f}[sec]".format(end_t-start_t))  # 1초 이하

"""
출력:
45725
0.0040[sec]
"""
