def solution(array):
    array.sort() #오름차순 정렬
    i = len(array)
    if i%2 == 0:
        i = int(i/2)
        answer = (array[i-1]+array[i])/2
    else:
        i = int(i/2)
        answer = array[i]
    return answer