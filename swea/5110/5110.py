import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = list(map(int, input().split()))
    for _ in range(M-1):
        temp = list(map(int, input().split()))
        idx = len(result)
        for i in range(len(result)):
            if result[i] > temp[0]:
                idx = i
                break
        result = result[:idx] + temp + result[idx:]
    print('#{} {}'.format(tc, ' '.join(map(str, list(reversed(result[-10:]))))))