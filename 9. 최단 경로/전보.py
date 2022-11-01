import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))

distance = [INF] * (n+1)
q = []
heapq.heappush(q, (0, c))
distance[c] = 0

while q:
    w, city = heapq.heappop(q)

    if distance[city] < w:
        continue

    distance[city] = w
    for i in graph[city]:
        cost = distance[city] + i[0]
        if distance[i[1]] > cost:
            distance[i[1]] = cost
            heapq.heappush(q, (cost, i[1]))

result = [x for x in distance if x < INF and x > 0]
count = len(result)
max_weight = max(result)

print(count, max_weight)