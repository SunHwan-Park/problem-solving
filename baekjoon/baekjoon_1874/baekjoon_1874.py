import sys
n = int(sys.stdin.readline())
result = ''
basic_list = list(range(1, n+1))
temp = []
stack = []
answer = []
for _ in range(n):
    k = int(sys.stdin.readline())
    answer.append(k)
    if len(temp) == 0:
        while basic_list[0] != k:
            temp.append(basic_list.pop(0))
            result += '+\n'
        temp.append(basic_list.pop(0))
        result += '+\n'
        stack.append(temp.pop())
        result += '-\n'
    else:
        if k == temp[-1]:
            stack.append(temp.pop())
            result += '-\n'
        elif k > temp[-1]:
            while basic_list[0] != k:
                temp.append(basic_list.pop(0))
                result += '+\n'
            temp.append(basic_list.pop(0))
            result += '+\n'
            stack.append(temp.pop())
            result += '-\n'
if stack == answer:
    print(result)
else:
    print('NO')