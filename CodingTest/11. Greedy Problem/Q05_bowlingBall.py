import random, time


def bowlingBall(N, balls):
    answer = 0  # 볼링공 고를 수 있는 경우의 수
    # Sort in ascending order
    balls.sort()

    for i in range(N-1):
        ball = balls[i]
        for j in range(i+1, N):
            if ball != balls[j]:
                answer += 1
    return answer


N,M = 1000, 10  # map(int, input().split())
balls = []
for _ in range(N):
    balls.append(random.randint(1,M))

# balls = # list(map(int, input().split()))
start_t = time.time()
print(bowlingBall(N, balls))
end_t = time.time()
print('Time: {:4f}[sec]'.format(end_t - start_t))

# 출력: 449831
# Time: 0.043997[sec]  -- limit: 1 sec
