def solution(lottos, win_nums):
    # 맞춘 갯수에 따른 등수
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    # 모르는 숫자 갯수와 맞춘 숫자 갯수 초기화
    unKnown, correctCnt = 0, 0
    
    for l in lottos:
        if l in win_nums:
            correctCnt += 1
        elif l == 0:
            unKnown += 1
    
    # 최고 순위, 최저 순위
    highest, lowest = rank[correctCnt + unKnown], rank[correctCnt]
    
    answer = [highest, lowest]
    return answer
