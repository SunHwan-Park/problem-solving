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