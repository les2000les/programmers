def solution(before, after):
    answer = 0
    before = sorted(before)
    after = sorted(after)
    before = ''.join(before)
    after = ''.join(after)
    if before == after:
        answer = 1
    else:
        answer = 0
    return answer