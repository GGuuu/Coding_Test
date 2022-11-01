import sys
input = sys.stdin.readline
INF = int(1e9)

# 입력 및 초기화
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

# 그래프 입력받기
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

# 자기 자신으로 가는 방향 0으로 설정
for i in range(1, n+1):
    graph[i][i] = 0

# 플로이드 워셜 알고리즘
for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)