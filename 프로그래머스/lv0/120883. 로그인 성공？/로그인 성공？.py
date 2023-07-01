def solution(id_pw, db):
    answer = ''
    idnum = []
    pw = []
    
    for i in range(len(db)):
        idnum.append(db[i][0])
    answer = idnum    
    for j in range(len(db)):
        pw.append(db[j][1])
    
    if id_pw[0] not in idnum:
        answer = "fail"
        return answer
    else:
        for xindex, x in enumerate(idnum):
            if x == id_pw[0]:
                pwindex = xindex
            else:
                continue
        if pw[pwindex] == id_pw[1]:
            answer = 'login'
        else:
            answer = 'wrong pw'
    return answer

#     for xindex, x in enumerate(idnum):
#         for yindex, y in enumerate(pw):
#             if xindex == yindex: #db 매칭
#                 if x == id_pw[0]: #아이디가 같은 경우
#                     if y == id_pw[1]: #비밀번호도 같은 경우
#                         answer = 'login'
#                         break
#                     else:
#                         answer = 'wrong pw'
#                         break
#                 else: #아이디가 다른 경우
#                     answer = 'fail'
#                     break
#             else:
#                 continue
                    
            
    return answer