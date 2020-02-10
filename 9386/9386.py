import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    text = input()+'*'
    max_len = 0
    temp_len = 0
    i = 0
    while i != N+1:
        if text[i] == '1':
            temp_len += 1
            i += 1
        else:
            if temp_len > max_len:
                max_len = temp_len
            temp_len = 0
            i += 1
    print('#{} {}'.format(tc, max_len))