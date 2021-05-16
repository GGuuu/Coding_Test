# 내 답과 책의 답이 같음
n, m = map(int, input().split())
maxNum = -1
for i in range(n):
    row = list(map(int, input().split()))
    minNum = min(row)

    if minNum>maxNum:
        maxNum = minNum

print(maxNum)