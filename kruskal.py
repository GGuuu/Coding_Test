#-*- coding:utf-8 -*-
import json
import math
import heapq


# def disjkstra(graph, start_address, end_address) :
#     distance = {}
#     distance[start_address] = [0, start_address]
#     q = []
#     heapq.heappush(q, [distance[start_address][0], start_address])
#     while q:
#         # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
#         current_distance, current_node = heapq.heappop(q)
#         # 현재 노드가 이미 처리된 적 있는 노드라면 무시
#         if current_node in distance.keys() and distance[current_node][0] < current_distance:
#             continue
#         # 현재 노드와 연결된 다른 인접한 노드들을 확인
#         for next_node, weight in graph[current_node].items():
#             total_distance = current_distance + weight
#             if next_node not in distance or total_distance < distance[next_node][0]:
#                 distance[next_node] = [total_distance, current_node]
#                 heapq.heappush(q, [total_distance, next_node])
#
#     path = end_address
#     path_output = end_address + '->'
#     while distance[path][1] != start_address:
#         path_output += distance[path][1] + '->'
#         path = distance[path][1]
#     path_output += start_address
#     print(path_output)
#
#     return distance


parent = dict()
rank = dict()


def find(node):
    # path compression 기법
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def make_set(node):
    parent[node] = node
    rank[node] = 0


def kruskal(graph):
    mst = list()

    # 1. 초기화
    for node in graph['vertices']:
        make_set(node)

    # 2. 간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort()

    # 3. 간선 연결 (사이클 없는)
    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)

    return mst


# 선택한 픽이 3개 이상일 경우를 기준으로 계산함
def find_shortest_route(event):
    # event 형식
    # {picks: [{address:주소, latitude:위도, longtitude:경도}]}

    # 서로 간의 거리 계산(유클리드 거리 계산)
    n = len(event)
    locations = {}
    for idx in range(len(event["picks"])):
        x, y, address = float(event["picks"][idx]['latitude']), float(event["picks"][idx]['longtitude']), event["picks"][idx]['address']
        locations[address] = [x, y]

    # 위도나 경도를 기준으로 정렬
    sorted_location = sorted(locations.items(), key=lambda x: x[1][0])  # 경도 기준 정렬
    ## locations.sort(key=lambda x:x[1]) # 위도 기준 정렬

    # 가까운 두 개의 노드끼리 연결
    n = len(locations)
    graph = {
        'vertices': [],
        'edges': []
    }

    for i in range(n):
        graph['vertices'].append(sorted_location[i][0])

        near = list()
        if i == 0:
            near.extend([i + 1, i + 2])
        elif i == n - 1:
            near.extend([i - 1, i - 2])
        else:
            near.extend([i - 1, i + 1])

        graph[sorted_location[i][0]] = {}
        x, y = map(float, sorted_location[i][1])
        for idx in near:
            nx, ny = map(float, sorted_location[idx][1])
            distance = float(math.sqrt((x - nx) ** 2 + (y - ny) ** 2))
            # graph[sorted_location[i][0]][sorted_location[idx][0]] = distance
            graph['edges'].append((distance, sorted_location[i][0], sorted_location[idx][0]))

    # dijkstra 알고리즘으로 최단 경로 도출
    # start = sorted_location[0][0]
    # end = sorted_location[-1][0]
    # distance = disjkstra(graph, start, end)
    # print(distance)

    # kruskal 알고리즘으로 최단 경로 도출
    shortest_ways = kruskal(graph)
    print(sorted_location)
    print(shortest_ways)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda'),
        'result': json.dumps(shortest_ways, ensure_ascii=False)
    }


if __name__ == '__main__':
    example = []

    # 임시 설정
    location1 = {'address': "임진각관광지", 'longtitude': 37.8893177, 'latitude': 126.740081}
    example.append(location1)

    location1 = {'address': "송정관광지", 'longtitude': 34.7231451, 'latitude': 128.0249666566}
    example.append(location1)

    location1 = {'address': "공릉관광지", 'longtitude': 37.7498111, 'latitude': 126.8335655}
    example.append(location1)

    location1 = {'address': "방화동가족휴가촌", 'longtitude': 35.59064179, 'latitude': 127.5268761}
    example.append(location1)

    ## # 지오코딩 추가
    # event : '{["address":"홍길동", "longtitude":29, "latitude":29, ...]}'
    # event = json.loads(event)
    event = {"picks":example}

    result = find_shortest_route(event)
    # print(result['result'])