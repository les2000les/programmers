def solution(emergency):
    answer = []
    rank = sorted(emergency)
    rank.reverse()
    for i in emergency:
        answer.append(rank.index(i)+1)
    return answer
