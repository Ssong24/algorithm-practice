# ** 8-1 1로 만들기 **
# Input: 26
# Output: 3
def toOne():
    n = int(input())  # 1 ~ 30,000
    d = [0] * (n+1)

    for x in range(2, n+1):
        # Current Num - 1
        d[x] = d[x-1] + 1
        # Get minimum result by comparing the case x is divided by 5/3/2
        if x % 5 == 0:
            d[x] = min(d[x], d[x//5] + 1)
        if x % 3 == 0:
            d[x] = min(d[x], d[x//3] + 1)
        if x % 2 == 0:
            d[x] = min(d[x], d[x//2] + 1)

    return d[n]

import time
start_time =  time.time()
print(toOne())
end_time = time.time()
print("Time: {}[sec]".format(end_time - start_time))
