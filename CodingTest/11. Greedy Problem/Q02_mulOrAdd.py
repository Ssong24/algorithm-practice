def mulOrAdd(numStr):
    op = 1  # 0: mul , 1: add
    answer = 0
    for s in numStr:
        num = int(s)  # character to integer
        answer = answer + num if op == 1 else answer * num  # By op code, run multiplication or addition
        op = 1 if num == 0 else 0  # if num is 0, next operation will be add. Else, next op is multiplication

    return answer

numStr = input()
print(mulOrAdd(numStr))
