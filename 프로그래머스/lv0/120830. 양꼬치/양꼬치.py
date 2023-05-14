def solution(n, k):
    k_service = int(n/10)
    answer = 12000*n + 2000*k - 2000*k_service
    return answer