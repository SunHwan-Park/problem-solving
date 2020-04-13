import sys
sys.stdin = open('input.txt')

# 1. test data 입력
T = int(input())
for tc in range(1, T+1):
    N, Q = list(map(int, input().split()))
    # 2. N개의 상자 생성
    box = [0 for _ in range(N)]
    # 3. Q회 만큼 작업 수행
    for i in range(1, Q+1):
        L, R = list(map(int, input().split()))
        for idx in range(L-1, R):
            box[idx] = i
    # 4. 결과 출력
    print('#{} {}'.format(tc, ' '.join(map(str, box))))