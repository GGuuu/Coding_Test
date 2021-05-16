import sys

n = int(sys.stdin.readline().rstrip())

q = []
for i in range(n):
    inputStr = sys.stdin.readline().rstrip()
    order = inputStr.split()[0]
    if order == 'push':
        num = int(inputStr.split()[1])
        q.append(num)
    elif order == 'pop':
        if len(q)<=0:
            print(-1)
        else:
            num = q.pop()
            print(num)
    elif order == 'size':
        print(len(q))
    elif order == 'empty':
        if len(q)<=0:
            print(1)
        else:
            print(0)
    elif order == 'top':
        if len(q) <= 0:
            print(-1)
        else:
            print(q[-1])