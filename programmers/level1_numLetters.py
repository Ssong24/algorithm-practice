def solution(s):
    # Dictionary key: letter for number,  value: number 
    dict_letter = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 
                   'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
   
    # Matched letters for check, answer number in string data type
    letters, ansStr = '', ''
    
    num_in_letters = list(dict_letter.keys())
    ASCII_0, ASCII_9 = ord('0'), ord('9')
    
    for i in s:
        if ASCII_0 <= ord(i) <= ASCII_9:
            ansStr += i
        else:
            letters += i
            if letters in num_in_letters:
                ansStr += dict_letter[letters]            
                letters = ''
                
    answer = int(ansStr)
    return answer
