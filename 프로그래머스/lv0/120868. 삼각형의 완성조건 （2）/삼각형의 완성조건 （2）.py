def solution(sides):
    answer = 0
    count = 0
    sum_len = 0 # 주어진 두 변의 길이의 합
    for i in sides:
        sum_len = sum_len +i
        
    for i in range(1, sum_len): # 나머지 한 변의 길이는 1~두 길이의 합
        if max(sides)>=i: #가장 긴 변이 sides중 하나일 경우
            if max(sides) < (sum_len-max(sides)) + i:
                count = count+1
            else:
                continue
        else: #가장 긴 변이 i
            if i<sum_len:
                count = count+1
            else:
                continue
    answer = count
            
            
    return answer