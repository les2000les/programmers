def solution(array):
    count = 0
    num = ''
    for i in str(array):
        if i == '7':
            count = count+1
        else: continue
    return count