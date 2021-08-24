from heapdict import heapdict
import math
import json


def get_route_by_prim(graph, start):
    mst, keys, pi, total_weight = list(), heapdict(), dict(), 0
    for node in graph.keys():
        keys[node] = float('inf')
        pi[node] = None
    keys[start], pi[start] = 0, start

    while keys:
        current_node, current_key = keys.popitem()
        mst.append([pi[current_node], current_node, current_key])
        total_weight += current_key
        for adjacent, weight in graph[current_node].items():
            if adjacent in keys and weight < keys[adjacent]:
                keys[adjacent] = weight
                pi[adjacent] = current_node

    route = []
    for i in mst[1:]:
        route.append(i[0])
    route.append(mst[-1][1])

    return route


def make_graph(picked_locations):
    # 서로 간의 거리 계산(유클리드 거리 계산)
    locations = {}
    for idx in range(len(picked_locations)):
        x, y, address = float(picked_locations[idx]['latitude']), float(picked_locations[idx]['longtitude']), \
                        picked_locations[idx]['address']
        locations[address] = [x, y]

    # 위도나 경도를 기준으로 정렬
    sorted_location = sorted(locations.items(), key=lambda x: x[1][0])  # 경도 기준 정렬
    # locations.sort(key=lambda x:x[1]) # 위도 기준 정렬

    # 가까운 두 개의 노드끼리 연결
    n = len(locations)
    graph = {

    }

    for i in range(n):
        near = []

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
            graph[sorted_location[i][0]][sorted_location[idx][0]] = distance

    start = sorted_location[0][0]

    return graph, start, locations


if __name__ == '__main__':
    # mygraph = {
    #     'A': {'B':7, 'D':5},
    #     'B' : {'A':7, 'D':9, 'C':8, 'E':7},
    #     'C':{'B':8, 'E':5},
    #     'D':{'A':5, 'B':9, 'E':7, 'F':6},
    #     'E':{'B':7, 'C':5, 'D':7, 'F':8, 'G':9},
    #     'F':{'D':6, 'E':8, 'G':11},
    #     'G':{'E':9, 'F':11}
    # }

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

    # 그래프 생성
    graph, start, location_points = make_graph(example)

    # 프림 알고리즘으로 최단 경로 도출
    route = get_route_by_prim(graph, start)
    print(route)

    for r in route:
        print(location_points[r])
