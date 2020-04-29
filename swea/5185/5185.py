import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, V = input().split()
    R = bin(int(V, 16))[2:]
    print('#{} {}'.format(tc, (int(N)*4 - len(R))*'0' + R))