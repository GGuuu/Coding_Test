# 내 답
n, k = map(int, input().split())

total = 0
while True:
    if n <= 1:
        break

    if n % k == 0:
        total += 1
        n //= k
    else:
        total += n%k
        n -= n%k

print(total)