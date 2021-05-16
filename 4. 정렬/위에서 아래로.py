# 내 답
n = int(input())

nums = []
for i in range(n):
    nums.append(int(input()))

'''
4
15
27
29
12
'''

# 선택 정렬
selectList = nums
for i in range(n):
    min_index = i
    for j in range(i, n):
        if selectList[min_index] < selectList[j]:
            min_index = j
    selectList[min_index], selectList[i] = selectList[i], selectList[min_index]

print(selectList)

# 삽입 정렬
insertList = nums
for i in range(1, n):
    insert_index = i
    for j in range(i, 0, -1):
        if insertList[i] > insertList[j]:
            insert_index = j
            break
    insertList[insert_index], insertList[i] = insertList[i], insertList[insert_index]

print(insertList)

# 퀵 정렬
quickList = nums


def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start+1
    right = end

    while left < right:
        while array[left] >= pivot and left < end:
            left += 1
        while array[right] <= pivot and right > start:
            right -= 1

        if left <= right:
            array[right], array[left] = array[left], array[right]
        else:
            array[right], array[pivot] = array[pivot], array[right]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(quickList, 0, len(quickList)-1)
print(quickList)

# 책의 답
array = sorted(nums, reverse=True)

print(array)