def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    
    # 2 ** ASCII_0에 ASCII_9를 넣어버림
    ASCII_a, ASCII_z = ord('a'), ord('z')
    ASCII_0, ASCII_9 = ord('0'), ord('9')
    for l in new_id:
        if ASCII_a <= ord(l) <= ASCII_z:
            answer += l
        elif ASCII_0 <= ord(l) <= ASCII_9:
            answer += l
        elif l in ['-', '_', '.']:
            answer += l
    
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    
    # 5
    if len(answer) == 0:
        answer += 'a'
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    # 7 ** 지문 읽다가 len(answer)에 len(new_id) 넣어버림
    while len(answer) <= 2:
        answer += answer[-1]
    
    return answer
