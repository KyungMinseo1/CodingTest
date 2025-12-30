# 게임 개발
def game():
    n, m = map(int, input().split())
    x, y, d = map(int, input().split())

    maps = []
    for _ in range(n):
        maps.append(list(map(int, input().split())))
    valid_maps = maps.copy()
    valid_maps[x][y] = 1

    # 북, 동, 남, 서 (현재 d에서 -1)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    start_d = d
    count = 1

    while True:
        if d > 0:
            d -= 1
        else:
            d = 3
        temp_x, temp_y = x + dx[d], y + dy[d]
        if d == start_d:
            if valid_maps[temp_x][temp_y] == 0 and maps[temp_x][temp_y] == 0:
                x, y = temp_x, temp_y
                valid_maps[x][y] = 1
                count += 1
                continue
            temp_d = (d+2)%4
            if maps[x+dx[temp_d]][y+dy[temp_d]] == 1:
                break
            else:
                x, y = x+dx[temp_d], y+dy[temp_d]
                continue
        if valid_maps[temp_x][temp_y] == 1 or maps[temp_x][temp_y] == 1:
            continue
        # if able to go
        x, y = temp_x, temp_y
        valid_maps[x][y] = 1
        start_d = d
        count += 1

    return count

if __name__=="__main__":
    print(game())