import heapq

def disjkstra(graph, start_address) :
    distance = {}
    distance[start_address] = 0
    q = []
    heapq.heappush(q, [distance[start_address], start_address])
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now_address = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if now_address in distance and distance[now_address] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now_address].keys():
            cost = dist + graph[now_address][i]
            if i not in distance or cost < distance[i]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

graph = {
    'a' : {'b':3, 'c':1},
    'b' : {'a':3, 'd':2},
    'c' : {'a':1, 'e':1},
    'd' : {'b':2, 'e':3},
    'e' : {'c':1, 'd':3}
}
start = 'a'

distance = disjkstra(graph, start)
print(distance)