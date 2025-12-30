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


if __name__=="__main__":
    print(udlr())