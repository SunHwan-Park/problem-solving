C, R = list(map(int, input().split()))
K = int(input())
 
if K > C*R:
    print('0')
else:
    i = 1
    while 2*i*(C+R) - (2*i-1)*(2*i+1) < K:
        i += 1
    if 2*i*(C+R) - (2*i-1)*(2*i+1) == K:
        i += 1
    result = [i, i]
    p = 2*(i-1)*(C+R) - (2*(i-1)-1)*(2*(i-1)+1)

    while p != K:
        while p != K and result[1] != R - i + 1:
            result[1] += 1
            p += 1
        while p != K and result[0] != C - i + 1:
            result[0] += 1
            p += 1
        while p != K and result[1] != i:
            result[1] -= 1
            p += 1
        while p != K and result[0] != i+1:
            result[0] -= 1
            p += 1

    print(' '.join(map(str, result)))