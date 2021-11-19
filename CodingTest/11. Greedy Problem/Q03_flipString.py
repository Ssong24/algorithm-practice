import random
import time


def flipString(sentence):
    answer = 0
    # 연속된 0과 1의 뭉텅이 갯수 세아림
    count = {'0':0, '1':0}

    # 첫 문자를 pre 변수에 초기화하고, count 증가하면서 시작
    pre = sentence[0]
    count[pre] += 1
    for now in sentence:
        if pre != now:  # 이전 숫자랑 달라지면 다른 부분.
            count[now] += 1

        pre = now
    answer = min(count.values())  # 더 적은 값을 answer로
    return answer


# 랜덤한 문자열 생성
n = 1000000 -1
sampleString = '01'
randomString = ''.join((random.choice(sampleString)) for x in range(n))
sentence = randomString #input()

start_t = time.time()
print(flipString(sentence))
end_t = time.time()
print("{:.4f}[sec]".format(end_t - start_t))
