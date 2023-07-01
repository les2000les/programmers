def solution(common):
    answer = 0
    if common[0] ==0:
        answer = common[len(common)-1] + (common[2]-common[1])
    else:
        if common[2]/common[1] == common[1]/common[0]:
            answer = common[len(common)-1] * (common[2]/common[1])
        else:
            answer = common[len(common)-1] + (common[2]-common[1])
        
    return answer