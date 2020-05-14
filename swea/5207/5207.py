import sys
sys.stdin = open('input.txt')

def f(l, r, d):
    mid = (l+r)//2
    if 'rr' in d or 'll' in d:
        return
    elif l > r:
        return
    elif l == r:
        psb_idx.add(mid)
        return
    else:    
        psb_idx.add(mid)
        f(mid+1, r, d+'r')
        f(l, mid-1, d+'l')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nlist = list(map(int, input().split()))
    mlist = set(map(int, input().split()))
    nlist.sort()
    psb_idx = set()
    f(0, len(nlist)-1, '')
    print('#{} {}'.format(tc, len(mlist & set(nlist[i] for i in psb_idx))))