import sys
from collections import deque
t = int(sys.stdin.readline().rstrip())
q = deque([])
for i in range(t):
    inputStr = sys.stdin.readline().rstrip()
    order = inputStr.split()[0]

    try:
        if order == 'push':
            num = int(inputStr.split()[1])
            q.append(num)
        elif order == 'pop':
            print(q.popleft())
        elif order == 'size':
            print(len(q))
        elif order == 'empty':
            if len(q) <= 0:
                print(1)
            else:
                print(0)
        elif order == 'front':
            print(q[0])
        elif order == 'back':
            print(q[-1])
    except:
        print(-1)
