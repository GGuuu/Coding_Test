from heapdict import heapdict
import math
import json
import requests
import xmltodict

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

    # example = []
    # # 임시 설정
    # location1 = {'address': "임진각관광지", 'longtitude': 37.8893177, 'latitude': 126.740081}
    # example.append(location1)
    # location1 = {'address': "송정관광지", 'longtitude': 34.7231451, 'latitude': 128.0249666566}
    # example.append(location1)
    # location1 = {'address': "공릉관광지", 'longtitude': 37.7498111, 'latitude': 126.8335655}
    # example.append(location1)
    # location1 = {'address': "방화동가족휴가촌", 'longtitude': 35.59064179, 'latitude': 127.5268761}
    # example.append(location1)
    #
    # # 그래프 생성
    # graph, start, location_points = make_graph(example)
    #
    # # 프림 알고리즘으로 최단 경로 도출
    # route = get_route_by_prim(graph, start)
    # print(route)
    #
    # for r in route:
    #     print(location_points[r])

    areaCode_dict = {
        '서울': '1',
        '강남구': '1-1',
        '강동구': '1-2',
        '강북구': '1-3',
        '강서구': '1-4',
        '관악구': '1-5',
        '광진구': '1-6',
        '구로구': '1-7',
        '금천구': '1-8',
        '노원구': '1-9',
        '도봉구': '1-10',
        '동대문구': '1-11',
        '동작구': '1-12',
        '마포구': '1-13',
        '서대문구': '1-14',
        '서초구': '1-15',
        '성동구': '1-16',
        '성북구': '1-17',
        '송파구': '1-18',
        '양천구': '1-19',
        '영등포구': '1-20',
        '용산구': '1-21',
        '은평구': '1-22',
        '종로구': '1-23',
        '중구': '1-24',
        '중랑구': '1-25',

        '인천': '2',
        '대전': '3',
        '대구': '4',
        '광주': '5',
        '부산': '6',
        '울산': '7',
        '세종특별자치시': '8',

        '경기도': '31',
        '가평군': '31-1',
        '고양시': '31-2',
        '과천시': '31-3',
        '광명시': '31-4',
        '광주시': '31-5',
        '구리시': '31-6',
        '군포시': '31-7',
        '김포시': '31-8',
        '남양주시': '31-9',
        '동두천시': '31-10',
        '부천시': '31-11',
        '성남시': '31-12',
        '수원시': '31-13',
        '시흥시': '31-14',
        '안산시': '31-15',
        '안성시': '31-16',
        '안양시': '31-17',
        '양주시': '31-18',
        '양평군': '31-19',
        '여주시': '31-20',
        '연천군': '31-21',
        '오산시': '31-22',
        '용인시': '31-23',
        '의왕시': '31-24',
        '의정부시': '31-25',
        '이천시': '31-26',
        '파주시': '31-27',
        '평택시': '31-28',
        '포천시': '31-29',
        '하남시': '31-30',
        '화성시': '31-31',

        '강원도': '32',
        '강릉시': '32-1',
        '고성군': '32-2',
        '동해시': '32-3',
        '삼척시': '32-4',
        '속초시': '32-5',
        '양구군': '32-6',
        '양양군': '32-7',
        '영월군': '32-8',
        '원주시': '32-9',
        '인제군': '32-10',
        '정선군': '32-11',
        '철원군': '32-12',
        '춘천시': '32-13',
        '태백시': '32-14',
        '평창군': '32-15',
        '홍천군': '32-16',
        '화천군': '32-17',
        '횡성군': '32-18',

        '충청북도': '33',
        '괴산군': '33-1',
        '단양군': '33-2',
        '보은군': '33-3',
        '영동군': '33-4',
        '옥천군': '33-5',
        '음성군': '33-6',
        '제천시': '33-7',
        '진천군': '33-8',
        '청원군': '33-9',
        '청주시': '33-10',
        '충주시': '33-11',
        '증평군': '33-12',

        '충청남도': '34',
        '공주시': '34-1',
        '금산군': '34-2',
        '논산시': '34-3',
        '당진시': '34-4',
        '보령시': '34-5',
        '부여군': '34-6',
        '서산시': '34-7',
        '서천군': '34-8',
        '아산시': '34-9',
        '예산군': '34-10',
        '천안시': '34-11',
        '청양군': '34-12',
        '태안군': '34-13',
        '홍성군': '34-14',
        '계룡시': '34-15',

        '경상북도': '35',
        '경산시': '35-1',
        '경주시': '35-2',
        '고령군': '35-3',
        '구미시': '35-4',
        '군위군': '35-5',
        '김천시': '35-6',
        '문경시': '35-7',
        '봉화군': '35-8',
        '상주시': '35-9',
        '성주군': '35-10',
        '안동시': '35-11',
        '영덕군': '35-12',
        '영양군': '35-13',
        '영주시': '35-14',
        '영천시': '35-15',
        '예천군': '35-16',
        '울릉군': '35-17',
        '울진군': '35-18',
        '의성군': '35-19',
        '청도군': '35-20',
        '청송군': '35-21',
        '칠곡군': '35-22',
        '포항시': '35-23',

        '경상남도': '36',
        '거제시': '36-1',
        '거창군': '36-2',
        '고성군': '36-3',
        '김해시': '36-4',
        '남해군': '36-5',
        '마산시': '36-6',
        '밀양시': '36-7',
        '사천시': '36-8',
        '산청군': '36-9',
        '양산시': '36-10',
        '의령군': '36-12',
        '진주시': '36-13',
        '진해시': '36-14',
        '창녕군': '36-15',
        '창원시': '36-16',
        '통영시': '36-17',
        '하동군': '36-18',
        '함안군': '36-19',
        '함양군': '36-20',
        '합천군': '36-21',

        '전라북도': '37',
        '고창군': '37-1',
        '군산시': '37-2',
        '김제시': '37-3',
        '남원시': '37-4',
        '무주군': '37-5',
        '부안군': '37-6',
        '순창군': '37-7',
        '완주군': '37-8',
        '익산시': '37-9',
        '임실군': '37-10',
        '장수군': '37-11',
        '전주시': '37-12',
        '정읍시': '37-13',
        '진안군': '37-14',

        '전라남도': '38',
        '강진군': '38-1',
        '고흥군': '38-2',
        '곡성군': '38-3',
        '광양시': '38-4',
        '구례군': '38-5',
        '나주시': '38-6',
        '담양군': '38-7',
        '목포시': '38-8',
        '무안군': '38-9',
        '보성군': '38-10',
        '순천시': '38-11',
        '신안군': '38-12',
        '여수시': '38-13',
        '영광군': '38-16',
        '영암군': '38-17',
        '완도군': '38-18',
        '장성군': '38-19',
        '장흥군': '38-20',
        '진도군': '38-21',
        '함평군': '38-22',
        '해남군': '38-23',
        '화순군': '38-24',

        '제주도': '39'
    }

    # 임시 설정 : 서울시 강남구
    serviceKey = 'HSqROv43%2B2Ke%2F46LOl9%2BVrwEjzb9ttKUi9%2B4RJxOaXnD3x%2B%2B1k3mBrzpURaf6kFEFxpW%2BmENjTXg6Avm%2BZfIrg%3D%3D'
    pageNo = '1'
    numOfRows = '20'
    MobileApp = 'AppTest'

    MobileOs = 'AND'
    arrange = 'O'

    contentTypeId = '12'
    areaCode = '1'
    sigunguCode = '1'
    listYN = 'Y'

    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?' \
          'serviceKey=' + serviceKey + \
          '&pageNo=' + pageNo + \
          '&numOfRows=' + numOfRows + \
          '&MobileApp=' + MobileApp + \
          '&MobileOS=' + MobileOs + \
          '&arrange=' + arrange + \
          '&contentTypeId=' + contentTypeId + \
          '&areaCode=' + areaCode + \
          '&sigunguCode=' + sigunguCode + \
          '&listYN=Y'

    res = requests.get(url)
    root = xmltodict.parse(res.text)
    dic = json.loads(json.dumps(root))
    itemList = dic['response']['body']['items']['item']

    print(itemList)

