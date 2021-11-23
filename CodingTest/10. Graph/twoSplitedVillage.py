import random
import time
import heapq

# Find
def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


# Union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# n: 집 갯수   m: 간선 갯수
MAX_N, MAX_M = 100000, 1000000
n, m = MAX_N, MAX_M  # map(int, input().split())

parent = [x for x in range(n+1)]  # Initialize parent node as itself
edges = []  # 간선 저장 리스트
# for i in range(m):
#     a, b, cost = map(int, input().split())
#     edges.append((cost, a, b))  # cost 기준으로 배열하기 위해 첫번째 원소로 지정

# 랜덤하게 숫자 생성
for i in range(m):
    [a,b] = random.sample(range(1, 100), 2)
    cost = random.randint(1, 1000)
    edges.append((cost, a, b))

start_t = time.time()
edges.sort()  # 오름차순으로 edges 나열

result = 0  # 마을 간 연결할 때 비용을 담을 변수
last = 0  # 두 마을로 분리 시 가장 큰 비용을 저장할 변수

for e in edges:
    cost, a, b = e

    # 사이클 없을 때 union 연산 시행(마을간 연결)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)
end_t = time.time()
print("Time: {:.4f}[sec]".format(end_t - start_t))

"""
n,m 최대치 설정 시
출력:
97
Time: 1.9304[sec]  (limit: 2 sec)
"""
