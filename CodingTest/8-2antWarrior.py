def antWarrior(n, storage):
    # Initiate DP table
    d = [0] * 100

    # Bottom-Up DP
    d[0] = storage[0]
    d[1] = max(storage[0], storage[1])
    for i in range(2, n):
        d[i] = max(d[i - 1], d[i - 2] + storage[i])

    print(d[n - 1])

import time
import random

# Get Input
# n = int(input())
# storage = list(map(int, input().split()))

# Time Test
n = 100
storage = random.sample(range(0, 1000), 100)

start = time.time()
antWarrior(n, storage)
end = time.time()

print("Time: {:5f}".format(end-start))
