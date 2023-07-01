def solution(n):
    
    n_list = [i for i in range(1, 230)]
    n2_list = []
    n3_list = []
    for i in n_list:
        if i%3 == 0: #3의 배수 제외
            continue
        else:
            n2_list.append(i)
            
    for j in n2_list:
        n2 = str(j)
        count =0
        for k in list(n2):
            if k == '3': #숫자3 포함 제외
                count = count+1
            else:
                continue
        if count == 0:
            n3_list.append(j)
        else:
            continue
    answer = n3_list[n-1]
    return answer