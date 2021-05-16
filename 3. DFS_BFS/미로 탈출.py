n, m = map(int, input().split())

miro = []
for i in range(n):
    array = list(map(int, input()))
    miro.append(array)


def shortest():
    queue = [[0, 0]]

    while len(queue)>0:
        x, y = queue.pop(0)
        if x+1 < n and miro[x+1][y] == 1:
            miro[x+1][y] += miro[x][y]
            queue.append([x+1, y])
        if x-1 > 0 and miro[x-1][y] == 1:
            miro[x-1][y] += miro[x][y]
            queue.append([x-1, y])
        if y+1 < m and miro[x][y+1] == 1:
            miro[x][y+1] += miro[x][y]
            queue.append([x, y+1])
        if y-1 > 0 and miro[x][y-1] == 1:
            miro[x][y-1] += miro[x][y]
            queue.append([x, y-1])

shortest()
print(miro[n-1][m-1])

'''
5 6
111110
111101
000101
111111
111111

3 4
1010
1100
0111
'''