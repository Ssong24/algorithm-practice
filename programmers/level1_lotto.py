def solution(lottos, win_nums):
    answer = []  # 최저, 최고 순위를 담을 배열
    prizeList = [6, 6, 5, 4, 3, 2, 1]  # 당첨된 번호 갯수를 인덱스해서 순위 저장한 배열
    
    lottoMax = 45  # 로또에서 가능한 최대 숫자
    check = [False] * (lottoMax + 1)  # 당첨된 번호의 결과를 저장
    unKnown = 0
    
    # 당첨 번호는 True
    for l in win_nums:
        check[l] = True
    
    # 로또 당첨된 번호 갯수 계산
    correctCnt = 0
    for n in lottos:
        if n == 0:
            unKnown += 1
        elif check[n]:
            correctCnt += 1
            
    # 최고 순위 번호
    answer.append(prizeList[correctCnt + unKnown])
    # 최저 순위 번호     
    answer.append(prizeList[correctCnt])
    
    
    return answer
