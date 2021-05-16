# 내가 짠 코드
n = int(input())
plan = input().split()

R = 1
L = -1
U = -1
D = 1

row = 1
col = 1
for i, char in enumerate(plan):
    if char == 'R' and col < n:
       col += 1
    elif char == 'L' and col > 1:
        col -= 1
    elif char == 'U' and row > 1:
        row -= 1
    elif char == 'D' and row < n:
        row += 1

print(row, col)

# 책의 코드
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]

    if nx<1 or ny<1 or nx>n or ny > n:
        continue

    x, y = nx, ny