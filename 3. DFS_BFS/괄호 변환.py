from collections import deque
input_str = input()


def fix_v(string):
    res = '('


def getRightSent(string):
    queue = deque([string[0]])
    u = ""
    v = ""
    temp = string[0]
    for s in string[1:]:
        if s==')':
            if len(queue)!=0:
                queue.popleft()
                temp += ')'
            else:
                temp += ')'
                v += temp
                temp = ""
        else:
            queue.append(s)
            temp += '('

        if len(queue) == 0:
            u += temp
            temp = ""

    if len(queue)>0:
        v += temp

    res = u
    if len(v)>0:
        res += getRightSent(v)

    return res

result = getRightSent(input_str)
print(result)