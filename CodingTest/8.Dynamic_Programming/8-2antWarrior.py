import time
import random


def antWarrior(n, storage):
    # DP table
    answer = storage.copy()

    # Bottom-Up
    for i in range(2, n):
        answer[i] = max(answer[i-2] + storage[i], answer[i-1])

    return answer[n-1]


# Create random list for testing time (limit: 1 sec)
n = 100  # int(input())
storage = random.sample(range(0, 1000), 100)  # list(map(int, input().split()))
start = time.time()
print(antWarrior(n,storage))
end = time.time()


print("Time: {:5f}".format(end-start))
