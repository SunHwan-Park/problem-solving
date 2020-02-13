import sys

T = int(sys.stdin.readline())
for _ in range(T):
    stack = []
    data = sys.stdin.readline().strip()
    for _ in range(25):
        try:
            data = data.replace('()', '')
        except:
            pass
    if data:
        print('NO')
    else:
        print('YES')




    # if len(data)%2 != 0 or data[0] == ')' or data[-1] == '(':
    #     print('No')
    # else:
    #     for i in range(len(data)):
    #         if len(stack) == 0 or data[i] == stack[-1]:
    #             stack.append(data[i])
    #         else:
    #             stack.pop()
    #     if stack:
    #         print('NO')
    #     else:
    #         print('YES')