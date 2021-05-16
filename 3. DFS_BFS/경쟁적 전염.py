from collections import deque

n, k = map(int, input().split())
virus_map = [[]]
virus_info = []
for i in range(1, n+1):
    virus_map.append([0]+list(map(int, input().split()))[:n])
    for j in range(1, n+1):
        if virus_map[i][j] != 0:
            virus_info.append([virus_map[i][j], 0, i, j])

s, x, y = map(int, input().split())

virus_info.sort()

q = deque(virus_info)

while q:
    v, n_s, n_x, n_y = q.popleft()

    if n_s == s:
        break
    dir = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    for d in dir:
        dx = n_x+d[0]
        dy = n_y+d[1]
        if 0 < dx <= n and 0 < dy <= n and virus_map[dx][dy] == 0:
            virus_map[dx][dy] = v
            q.append([virus_map[dx][dy], s+1, dx, dy])

print(virus_map[x][y])