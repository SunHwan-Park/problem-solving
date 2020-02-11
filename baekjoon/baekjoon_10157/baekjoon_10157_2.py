C, R = list(map(int, input().split()))
K = int(input())
 
if K > C*R:
    print('0')
else:
    result = [1, 1]
    i = 1
    low_R = 1
    low_C = 2
       
    while i != K and i != C*R:
        while i != K and result[1] != R:
            result[1] += 1
            i += 1
        while i != K and result[0] != C:
            result[0] += 1
            i += 1
        while i != K and result[1] != low_R:
            result[1] -= 1
            i += 1
        while i != K and result[0] != low_C:
            result[0] -= 1
            i += 1
        R -= 1
        C -= 1
        low_R += 1
        low_C += 1

    print(' '.join(map(str, result)))