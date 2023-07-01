def solution(chicken):
    answer = 0
    num = []
    for i in range(1, len(str(chicken))+1):
        if chicken >=10:
            numb = chicken%10 # 나머지
            numa = (chicken-numb)/10 #몫 : 서비스개수
            chicken = numa + numb #서비스로 받은 치킨의 쿠폰+원래 쿠폰
            answer = answer + numa
        else: continue
    return answer