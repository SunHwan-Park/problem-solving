import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    text = input()
    for vowel in ['a', 'e', 'i', 'o','u']:
        text = text.replace(vowel, '')

    print('#{} {}'.format(tc, text))