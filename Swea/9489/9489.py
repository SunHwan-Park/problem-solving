import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    max_len = 0
    temp_len_r = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                temp_len_r += 1
            else:
                if temp_len_r > max_len:
                    max_len = temp_len_r
                temp_len_r = 0
        if temp_len_r > max_len:
            max_len = temp_len_r
        temp_len_r = 0

    temp_len_c = 0
    for k in range(M):
        for l in range(N):
            if matrix[l][k] == 1:
                temp_len_c += 1
            else:
                if temp_len_c > max_len:
                    max_len = temp_len_c
                temp_len_c = 0
        if temp_len_c > max_len:
            max_len = temp_len_c
        temp_len_c = 0

    print('#{} {}'.format(tc, max_len))

# -----------------------------------
# 홍주표 코드
def find(area):
    max_ruin = 0
    for line in area:
        for ruin in line.split('0'):
            now = len(ruin)
            if now > max_ruin:
                max_ruin = now
    return max_ruin

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    area = [''.join(
        input().split()) for _ in range(n)]
    width = find(area)
    vertical = [''.join(line) for line in list(zip(*area))]
    height = find(vertical)
    result = max(width, height)
    print('#{0} {1}'.format(tc, result))