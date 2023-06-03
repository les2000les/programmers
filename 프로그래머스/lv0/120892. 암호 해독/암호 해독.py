def solution(cipher, code):
    answer = ''
    for j in range(0, len(cipher)):
        if (j+1)%code ==0:
            answer = answer+ cipher[j]
        else:
            continue
    return answer