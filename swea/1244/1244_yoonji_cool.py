import sys
sys.stdin = open('input.txt')

def f(c, chk_cnt):
    temp = int(''.join(c))
    if temp > maxnum[chk_cnt]:
        maxnum[chk_cnt] = temp
    else:
        return
    if chk_cnt == cnt:
        return
    for i in range(cardlen):
        for j in range(i+1, cardlen):
            c[i], c[j] = c[j], c[i]
            f(c, chk_cnt+1)
            c[i], c[j] = c[j], c[i]

T = int(input())

for tc in range(1, T+1):
    d, cnt = input().split()
    cnt = int(cnt)
    cards = list(d)
    cardlen = len(cards)
    maxnum = [0]*(cnt+1)
    f(cards, 0)
    print(f'#{tc} {maxnum[-1]}')