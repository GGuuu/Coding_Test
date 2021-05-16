# 내 답
n = int(input())
student_info = []


def quick_sort(info):
    if len(info) == 1:
        return info
    pivot = info[0][1]

    left = [x for x in info if x[1] < pivot]
    right = [x for x in info if x[1] >= pivot]

    smaller = quick_sort(left)
    larger = quick_sort(right)

    return smaller+larger

for i in range(n):
    info = input().split()
    student_info.append([info[0], int(info[1])])

result = quick_sort(student_info)
print(result)

# 책의 답
array = sorted(student_info, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')