def solution(num_list, n):
    answer = [num_list[i-n:i] for i in range(n, len(num_list)+1, n)] 
    return answer