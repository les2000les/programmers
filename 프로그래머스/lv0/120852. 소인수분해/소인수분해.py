def solution(n):
    answer = []
    num = []
    for i in range(2, n+1):
        while n%i == 0:
            num.append(i)
            n = int(n/i)
    for j in num:
        if j not in answer:
            answer.append(j)
    return answer