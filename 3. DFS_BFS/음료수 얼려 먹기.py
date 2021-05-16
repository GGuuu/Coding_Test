# 내 답
n, m = map(int, input().split())

tray = []
for i in range(n):
    array = list([int(x) for x in input()])
    tray.append(array)


def make_one(tray, x, y):
    tray[x][y] = 1

    queue = [[x, y]]
    while len(queue)>0:
        x, y = queue.pop(0)
        if x-1 > 0 and tray[x-1][y]==0:
            queue.append([x-1, y])
            tray[x-1][y] = 1
        if x+1 < n and tray[x+1][y]==0:
            queue.append([x+1, y])
            tray[x+1][y] = 1
        if y-1 > 0 and tray[x][y-1]==0:
            queue.append([x, y-1])
            tray[x][y-1] = 1
        if y+1 < m and tray[x][y+1]==0:
            queue.append([x, y+1])
            tray[x][y+1] = 1


result = 0
for i in range(n):
    for j in range(m):
        if tray[i][j] == 0:
           make_one(tray, i, j)
           result += 1

print(result)

'''
4 5
00110
00011
11111
00000
'''

# 책의 답
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x<= -1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)