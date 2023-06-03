def solution(hp):
    answer = 0
    while hp>0:
        if int(hp/5)>0:
            answer = answer+ int(hp/5)
            hp = hp%5
        else:
            if int(hp/3)>0:
                answer = answer+ int(hp/3)
                hp = hp%3
            else:
                answer = answer + hp
                break          
    return answer