def solution(s):
    answer = []
    sol_in = []
    sol_out = []
    strlist = list(s)
    for i in s:
        if i not in sol_in:
            sol_in.append(i)
        else:
            sol_out.append(i) #중복된 문자
    for j in sol_in:
        if j not in sol_out: # 중복된 문자 안에 없다면
            answer.append(j) #내가 찾는 답
        else:
            continue
    answer.sort()
    answer = ''.join(answer)
    return answer