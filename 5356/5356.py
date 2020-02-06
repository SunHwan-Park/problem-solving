import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    words = [input() for _ in range(5)]
    max_length = max([len(word) for word in words])
    answer = ''
    for idx in range(max_length):
        for word in words:
            try:
                answer += word[idx]
            except:
                pass

    print('#{} {}'.format(tc, answer))