n, m = map(int, input().split())
x, y, looking_side = map(int, input().split())

game_map = []
for i in range(n):
    game_map.append(list(map(int, input().split())))

# 순서대로 북, 동, 남, 서
side_map = [[-1,0],[0,1],[1,0],[0,-1]]
result = 1

game_map[x][y] = 1
while True:
    moved = False

    for i in range(1, 4):
        dx, dy = side_map[looking_side-i]
        if game_map[x+dx][y+dy] == 0:
            x += dx
            y += dy

            looking_side = (looking_side-i+4)%4
            game_map[x][y] = 1
            moved = True

            result += 1
            break

    if not moved:
        dx, dy = side_map[(looking_side + 2) % 4]
        if game_map[x+dx][y+dy] == 0:
            x = x+dx
            y = y+dy
            result += 1
            game_map[x][y] = 1
        else:
            break

print(result)
