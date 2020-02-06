import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    d = input()

    line1_5 = '..'
    line2_4 = '.'
    line3 = '#.'

    for char in d:
        line1_5 += '#...'
        line2_4 += '#.#.'
        line3 += char+'.#.'

    print(line1_5[0:5*len(d)-(len(d)-1)])
    print(line2_4[0:5*len(d)-(len(d)-1)])
    print(line3[0:5*len(d)-(len(d)-1)])
    print(line2_4[0:5*len(d)-(len(d)-1)])
    print(line1_5[0:5*len(d)-(len(d)-1)])

# ----------------------------------
# 강사님 코드

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    text = input()
    length = len(text)
    print('..'+'...'.join('#'*length)+'..')
    print('.#' + '#.#'.join('.'*length) + '#.')
    print('#.' + '.#.'.join(text) + '.#')
    print('.#' + '#.#'.join('.'*length) + '#.')
    print('..'+'...'.join('#'*length)+'..')