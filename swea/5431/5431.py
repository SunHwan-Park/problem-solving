import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    student = list(map(int, input().split()))
    result = []
    for i in range(1, N+1):
        if i not in student:
            result.append(i)
    print('#{} {}'.format(tc, ' '.join(map(str, result))))
