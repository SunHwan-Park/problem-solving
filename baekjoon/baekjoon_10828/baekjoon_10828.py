import sys

data = []
n = int(sys.stdin.readline())
for _ in range(n):
    command = sys.stdin.readline().split()
    C = command[0]
    if C == 'push':
        data.append(command[1])
    elif C == 'pop':
        try:
            print(data.pop())
        except:
            print(-1)
    elif C == 'size':
        print(len(data))
    elif C == 'empty':
        if data:
            print(0)
        else:
            print(1)
    elif C == 'top':
        try:
            print(data[-1])
        except:
            print(-1)

# -------------------------------
# 강사님 코드
import sys

T = int(sys.stdin.readline())
stack = []
for _ in range(T):
    D = sys.stdin.readline().split()
    if D[0] == 'push':
        stack.append(D[1])
    elif D[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif D[0] == 'size':
        print(len(stack))
    elif D[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif D[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)