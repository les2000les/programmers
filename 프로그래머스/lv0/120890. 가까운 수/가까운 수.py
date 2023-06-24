def solution(array, n):
    answer = 0
    minvalue = max(array)
    mini = min(array)
    for i in array:
        if abs(i-n) < minvalue:
            minvalue = abs(i-n)
            mini = i
        elif abs(i-n) ==minvalue:
            if i< minvalue+n:
                mini = i
            else:
                continue
        else:
            continue
    answer = mini
    return answer