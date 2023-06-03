def solution(numbers):
    maxvalue = -100000000
    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers):
            if i == j:
                continue
            else:
                if x*y > maxvalue:
                    maxvalue = x*y
                else:
                    continue
    answer = maxvalue
    return answer