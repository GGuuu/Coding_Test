# 내 답
place = input()
rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x, y = rows.index(place[0])+1, int(place[1])

moves = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]

result = 0
for move in moves:
    if x+move[0] > 0 and x+move[0]<=8 and y+move[1]>0 and y+move[1]<=8:
        result += 1

print(result)

# 책의 답
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a'))+1

steps = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]

result = 0
for step in steps:
    next_row = row+step[0]
    next_column = column+step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)