# 상하 좌우
def udlr():
    n = int(input())
    move = list(map(str, input().split()))

    move_id = ['L', 'R', 'U', 'D']
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    loc = [1,1]

    for m_id in move:
        idx = move_id.index(m_id)
        n_dx, n_dy = dx[idx], dy[idx]
        n_locx, n_locy = loc[0]+n_dx, loc[1]+n_dy
        if n_locx < 1 or n_locx > n or n_locy < 1 or n_locx > n:
            continue
        loc[0], loc[1] = n_locx, n_locy
    return str(loc[0]) + " " + str(loc[1])

# 시각
def time():
    n = int(input())
    valid_in_60 = 0

    for minute in range(60):
        if "3" in str(minute):
            valid_in_60 += 1

    total_valid = valid_in_60 * 60 # for valid minute
    not_valid_min = 60-valid_in_60 # not valid minutes
    extra_valid = not_valid_min*valid_in_60

    total_valid += extra_valid

    total = 0
    for h in range(n+1):
        if "3" in str(h):
            total += 60*60
        else:
            total += total_valid

    return total

def knight(): # ord() 쓰는 방식도 존재
    loc = str(input())
    x_loc, y_loc = loc[0], loc[1]

    x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    y = ['1', '2', '3', '4', '5', '6', '7', '8']

    dx = [-2, -2, 2, 2, -1, 1, -1, 1]
    dy = [-1, 1, -1, 1, -2, -2, 2, 2]

    current_loc = [x.index(x_loc), y.index(y_loc)]
    count = 0

    for cdx, cdy in zip(dx, dy):
        ndx, ndy = current_loc[0]+cdx, current_loc[1]+cdy
        if ndx < 0 or ndx > len(x)-1 or ndy < 0 or ndy > len(y)-1:
            continue
        count += 1

    return count

if __name__=="__main__":
    print(knight())