import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E, num1, num2 = map(int, input().split())
    D = list(map(int, input().split()))
    parents = [0]*(V+1)
    parents[0] = ''
    for i in range(E):
        parents[D[2*i+1]] = D[2*i]
    share = []
    while True:
        try:
            if parents[num1] in share:
                result = parents[num1]
                break
            else:
                share.append(parents[num1])
                num1 = parents[num1]
        except:
            pass
        try:
            if parents[num2] in share:
                result = parents[num2]
                break
            else:
                share.append(parents[num2])
                num2 = parents[num2]
        except:
            pass
 
    queue = [result]
    cnt = 1
    while queue:
        temp = queue.pop(0)
        for i in range(1, V+1):
            if parents[i] == temp:
                cnt += 1
                queue.append(i)
 
    print('#{} {} {}'.format(tc, result, cnt))