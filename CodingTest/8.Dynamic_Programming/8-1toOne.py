# ** 1로 만들기 **
# Input 26
# Output 3
import time

def toOne(n):
    # Initialize the DP table
    answer = [0] * (n+1)

    for i in range(2, n+1):
        # Calculate the one-deducted case, then compare with division of 5/3/2.
        answer[i] = answer[i-1] + 1

        # If num is divided by 5 or 3 or 2, compare its calculation count with each one.
        if i % 5 == 0:
            answer[i] = min(answer[i//5] + 1, answer[i])
        if i % 3 == 0:
            answer[i] = min(answer[i//3] + 1, answer[i])
        if i % 2 == 0:
            answer[i] = min(answer[i//2] + 1, answer[i])

    print(answer[n])

# Get input
n = int(input()) # 1 ~ 30,000

# Measure the time (limit: 1 sec)
start_time = time.time()
toOne(n)
end_time = time.time()
print("Time: {:.4f}[sec]".format(end_time - start_time))
