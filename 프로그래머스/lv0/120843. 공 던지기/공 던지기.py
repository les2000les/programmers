def solution(numbers, k):
    answer = 0
    numbers = numbers*k
    answer = numbers[2*k-2]
    return answer