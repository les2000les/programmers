def solution(num, k):
    find = str(num).find(str(k))
    if find == -1:
        answer = -1
    else:
        answer = find+1
    return answer