# 내 답
n = int(input())

three = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]

result = 0
for hour in range(n+1):
    if hour in three:
        result += 60*60
    else:
        for min in range(60):
            if min in three:
                result += 60
            else:
                result += len(three)

print(result)

# 책의 답
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)