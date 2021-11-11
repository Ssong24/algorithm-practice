def solution(numbers, hand):
    left_nums = [1,4,7]
    right_nums = [3,6,9]
    answer = ''
    # 숫자(index)마다 위치 
    rows=[3,0,0,0,1,1,1,2,2,2]
    cols=[1,0,1,2,0,1,2,0,1,2]
    
    # 초기 왼손, 오른손의 위치 
    left_hand, right_hand = (3,0), (3,2)
    
    for n in numbers:
        curPos = (rows[n], cols[n])
        if n in left_nums:  # 1,4,7일 경우 L
            answer += 'L'            
            left_hand = curPos  # 왼손 위치 갱신
        elif n in right_nums:  # 3,6,9일 경우 R
            answer += 'R'            
            right_hand = curPos  # 오른손 위치 갱신
        else: # 2,5,8,0일 경우 거리 계산  pow(,2)이 아닌 abs() 써야 통과됨 
            # 정답 맞아도 시간 많이 걸리면 실패라고 뜸
            left_cost = abs(curPos[0]-left_hand[0]) + abs(curPos[1]-left_hand[1])
            right_cost = abs(curPos[0]-right_hand[0]) + abs(curPos[1]-right_hand[1])
            if left_cost < right_cost:
                answer += 'L'
                left_hand = curPos
            elif left_cost > right_cost:
                answer += 'R'
                right_hand = curPos
            else:  ## cost is same
                if hand == "left":
                    answer += 'L'
                    left_hand=curPos
                elif hand == "right":
                    answer += 'R'
                    right_hand=curPos
                else:
                    print("Check 'hand' input")
    
    
    
    return answer
