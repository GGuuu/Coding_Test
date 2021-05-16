n, m = map(int, input().split())

arr = [x for x in range(1, n+1)]

print('<', end='')
idx = 0
for i in range(1,n+1):
    idx += m-1
    idx %= len(arr)
    if len(arr) == 1:
        print(arr[idx], end='')
    else:
        print(arr[idx], end=', ')
    arr.pop(idx)
print('>')
