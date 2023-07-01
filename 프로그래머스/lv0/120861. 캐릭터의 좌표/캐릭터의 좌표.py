def solution(keyinput, board):
    answer = []
    garo = (board[0]-1)/2
    sero = (board[1]-1)/2
    x = 0
    y = 0
    for key in keyinput:
        if key == 'left':
            if x > -garo:
                x = x - 1
            else:
                continue
        elif key == 'right':
            if x < garo:
                x = x + 1
            else:
                continue
        elif key == 'up':
            if y < sero:
                y = y + 1
            else:
                continue
        elif key == 'down':
            if y > -sero:
                y = y - 1
            else:
                continue
        else:
            continue
    answer = [x,y]
    return answer