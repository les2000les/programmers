def solution(num, total):
    answer = []
    mid = int(total/num)
    answer.append(mid)
    if num%2 == 0:
        for i in range(1, int((num-1)/2)+1):
            answer.append(mid-i)
        for j in range(1, int((num-1)/2)+2):
            answer.append(mid+j)
    else:
        for i in range(1, int((num-1)/2)+1):
            answer.append(mid-i)
        for j in range(1, int((num-1)/2)+1):
            answer.append(mid+j)
    answer.sort()
    return answer