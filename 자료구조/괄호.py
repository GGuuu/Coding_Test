import sys
t = int(sys.stdin.readline().rstrip())

for i in range(t):
    string = input()
    n = 0
    for s in string:
        if s == '(':
            n += 1
        else:
            n -= 1
            if n < 0:
                break

    if n == 0:
        print("YES")
    else:
        print("NO")