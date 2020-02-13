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