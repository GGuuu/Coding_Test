# 내 답
n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

arrA = a
arrB = b

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]

    left = [x for x in array if x < pivot]
    pivots = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quick_sort(left) + pivots + quick_sort(right)


arrA = quick_sort(arrA)
arrB = quick_sort(arrB)

for i in range(k):
    arrA[i], arrB[n-1-i] = arrB[n-1-i], arrA[i]

print(sum(arrA))

# 책의 답
a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
