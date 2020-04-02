import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    D = list(enumerate(C))

    temp = []
    for _ in range(N):
        temp.append(D.pop(0))

    while len(temp) > 1:
        if temp[0][1] == 0:
            if D:
                temp[0] = D.pop(0)
            else:
                temp.pop(0)
        else:
            temp.append((temp[0][0], temp[0][1]//2))
            temp.pop(0)
    print('#{} {}'.format(tc, temp[0][0]+1))