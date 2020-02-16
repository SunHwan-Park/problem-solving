import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = input().split()
    front = cards[:N//2 + N%2]
    back = cards[N//2 + N%2:]

    result = ''
    for i in range(N//2 + N%2):
        result += front[i] + ' '
        try:
            result += back[i] + ' '
        except:
            pass
    print('#{} {}'.format(tc, result))