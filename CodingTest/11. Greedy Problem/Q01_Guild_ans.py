# 답안 예시 + 시간 체크
import random, time
MAX = 100000
n = MAX  # int(input())
# data = list(map(int, input().split()))
data = []
for _ in range(n):
    data.append(random.randint(1, 5))

start_t = time.time()
data.sort()  # 오름차순으로 정렬

result = 0  # 총 그룹 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in data:
    count += 1
    if count >= i:  # 현재 그룹에 포함된 모험가 수가 현재 공포도 이상이면
        # 그룹 결성
        result += 1  # 총 그룹 수 증가
        count = 0  # 현재 그룹에 포함된 모험가 수 초기화

print(result)

end_t = time.time()
print("{:.4f}[sec]".format(end_t-start_t))

"""
출력:
45694
0.0190[sec]
"""
