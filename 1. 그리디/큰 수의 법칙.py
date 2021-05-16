# 내가 짠 부분
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0
for i in range(1, m+1):
    if i % (k+1) == 0:
        result += second
    else:
        result += first

print(result)

# 교재에 나와있는 부분
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
secode = data[n-2]

## 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m%(k+1)

result = 0
result += count * first # 가장 큰 수 더하기
result += (m-count) * secode # 두 번째로 큰 수 더하기

print(result)