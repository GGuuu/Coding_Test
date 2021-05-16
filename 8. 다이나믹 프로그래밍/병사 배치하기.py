# 인터넷 보고 배낀 답
n = int(input())
soldier = list(map(int, input().split()))

reversed(soldier)

num_solier = [1]*n

for i in range(len(soldier)):
    for j in range(i):
        if soldier[i] < soldier[j]:
            num_solier[i] = max(num_solier[i], j+1)

print(n-max(num_solier))
