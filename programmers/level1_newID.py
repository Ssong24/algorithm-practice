def solution(new_id):
    answer = ''
    # stage 1
    new_id = new_id.lower()

    # stage 2
    for l in new_id:
        if ord("a") <= ord(l) <= ord("z"):
            answer+=l
        elif ord('0') <= ord(l) <= ord('9'):
            answer += l
        elif l in ["-", "_", "."]:
            answer+=l
    
    # stage 3
    while '..' in answer:
        answer = answer.replace("..", ".")

    
    # stage 4
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    
    # stage 5
    if len(answer) == 0:
        answer += "a"
        
    # stage 6
    limit=16
    if len(answer) >= limit:
        answer = answer[:limit-1]
        if answer[-1] =='.':
            answer = answer[:-1]
            
    # stage 7
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
            
    return answer
