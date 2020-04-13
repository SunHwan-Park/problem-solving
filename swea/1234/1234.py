import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N, text = input().split()
    count = 1
    while count != 0:
        count = 0
        for i in range(len(text) - 1):
            if text[i] == text[i+1]:
                try:
                    text = text[:i] + text[i+2:]
                except:
                    text = text[:i]
                count += 1
                break
    print('#{} {}'.format(tc, text))
