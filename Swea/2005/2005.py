# 2005
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # 틀 만들기
    base = []
    for i in range(n):
        base.append([0] * (i + 1))
	
    # 조건에 맞춰 값 바꿔주기
    for idx in range(n):
        for k in range(idx + 1):
            if idx > 1 and k != 0 and k != idx:
                base[idx][k] = base[idx - 1][k - 1] + base[idx - 1][k]
            else:
                base[idx][k] = 1
                
    print('#{}'.format(tc))
    for i in range(n):
        print(' '.join(list(map(str, base[i]))))

# ------------------------------------
# 강사님 코드_재귀

# 재귀에서 생각해야할 것!
# 1. base case
# - 정답을 찾았을 때
# - 정답을 찾지 못했을 때
# 2. recursive step: 계속 가야할 때

# * 데이터(누적): 인자

import sys
sys.stdin = open('input.txt')

def pascal(x, y):
    if y == 0 or x == y: # 정답을 찾았을 때
        return 1
    # elif y < 0 or x < y: # 정답을 찾지 못했을 때
    #     return 0
    return pascal(x-1, y-1) + pascal(x-1, y)

T = int(input())
for tc in range(1, T+1):
    print('#{} '.format(tc))
    N = int(input())
    for i in range(N):
        for j in range(i+1):
            print(pascal(i, j), end=' ')
        print()

# ---------------------------------------
# 강사님 코드_김탁기 대표 버전
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{} '.format(tc))
    N = int(input())
    temp = []
    # result = [1]
    print(1)
    for i in range(N-1):
        result = [1]
        for j in range(i):
            result.append(temp[j] + temp[j+1])
        result.append(1)
        print(' '.join(map(str, result)))
        temp = result

# -----------------------------------------
# 강사님 코드
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{} '.format(tc))
    N = int(input())
    
    prev_line = [0, 1, 0]
    print(''.join([str(n) for n in prev_line[1:-1]]))
    for length in range(2, N+1):
        curr_line = [0] + [prev_line[i] + prev_line[i+1] for i in range(length)] + [0]
        print(' '.join([str(n) for n in curr_line[1:-1]]))
        prev_line = curr_line