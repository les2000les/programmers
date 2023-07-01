def solution(spell, dic):
    answer = 0
    num = 0
    for i in dic:
        arr = []
        for k in list(i):
            if k not in arr:
                arr.append(k)
            else:
                continue
        arr = ''.join(arr)
        count = 0
        for j in spell:
            if arr.find(j) !=-1:
                count = count+1
            else:
                continue
        if count == len(i) and  len(spell) == len(i):
            num = num+1
        else:
            continue
    if num >= 1:
        answer = 1
    else:
        answer = 2
    return answer