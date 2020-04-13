import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    D = list(input())
    numbers = []
    for _ in range(N//4):
        for i in range(4):
            numbers.append(''.join(D[N//4*i:N//4*(i+1)]))
        D.insert(0, D.pop())
    print('#{} {}'.format(tc, int(sorted(list(set(numbers)), reverse=True)[K-1], 16)))