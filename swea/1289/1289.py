import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    d = input()
    start = '0' * len(d)
    count = 0
    for i in range(len(d)):
        if d[i] != start[i]:
            start = start[:i] + len(start[i:])*d[i]
            count += 1
    print('#{} {}'.format(tc, count))