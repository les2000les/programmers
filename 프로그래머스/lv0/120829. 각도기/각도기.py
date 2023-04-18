def solution(angle):
    if 0 < angle < 90: #예각
        answer = 1
    elif angle == 90: #직각
        answer = 2
    elif 90 < angle < 180: #평각
        answer = 3
    else:
        answer = 4
    return answer