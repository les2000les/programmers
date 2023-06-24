def solution(i, j, k):
    num = [x for x in range(i, j+1)]
    num = ''.join(str(num))
    num = list(num)
    count = 0
    for y in num:
        if str(y).find(str(k)) != -1:
            count = count + 1
        else:
            continue
    answer = count
    return answer




