import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = float(input())
    answer = ''
    k = -1
    while N > 0:
        if len(answer) > 12:
            answer = 'overflow'
            break
        elif N >= 2**(k):
            answer += '1'
            N -= 2**(k)
        else:
            answer += '0'
        k -= 1
    print(f'#{tc} {answer}')