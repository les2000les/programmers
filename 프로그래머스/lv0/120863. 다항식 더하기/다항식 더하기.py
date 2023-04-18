def solution(polynomial):
    answer = ''
    xlist = []
    noxlist = []
    polylist = []
    noxsum = 0
    xsum = 0
    
    poly = polynomial.split(' ') #다항식을 공백단위로 잘라
    poly = list(poly) #list에 넣음
    
    for x in poly: #list에서 for문을 돌면서
        if x =='+': #값이 +인 경우
            continue #지나감
        else: #그 외인 경우
            polylist.append(x) #새 list에 저장
        
    for y in polylist: #새 list를 for문으로 돌며
        if 'x' in y:
            xlist.append(y)
        else:
            noxlist.append(y)
    
    for z in noxlist:
        noxsum += int(z)
    
    for k in xlist:
        if k == 'x':
            xsum +=1
        else:
            k = str(k).strip('x')
            xsum += int(k)
            
            
            
    if xsum == 0:
        pass
    elif xsum == 1:
        xsum ='x'
    else:
        xsum = str(xsum)+'x'
    
    
    if noxsum == 0 and xsum ==0:
        answer ="0"
    elif noxsum == 0:
        answer = xsum
    elif xsum == 0:
        answer = str(noxsum)
    else:
        answer = str(xsum) +' + ' +str(noxsum)
    return answer