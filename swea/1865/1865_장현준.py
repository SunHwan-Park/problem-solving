import sys
sys.stdin = open('input.txt')

def go(s, percent):
    v = []
    res = 0
    while s:
        r, c = s.pop() # v도착후 행동
        now = percent.pop() #확률
        while len(v) != r:
            v.pop()
        v.append(c)
 
        if now > res: #백트래킹
            if r == N-1: # 일 분배완료 & now > res
                res = now
            else:
                for w in range(N): #w서치
                    if w not in v:
                        s.append((r+1, w))
                        percent.append(now*field[r+1][w])
    return res
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = list( [float(n)/100 for n in input().split() ] for _ in range(N))
    #초기값
    s = [(0, i) for i in range(N)]
    percent = [n for n in field[0]]
    print('#{0} {1:00.6f}'.format(tc, go(s, percent)*100 ))