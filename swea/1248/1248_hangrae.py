import sys
sys.stdin = open('input.txt')

T= int(input())
for tc in range(1,T+1):
    V, E, x, y = map(int,input().split())
    p = [i for i in range(V+1)]
    arr = list(map(int,input().split()))
    for i in range(E):
        parent, child= arr[2*i], arr[2*i+1]
        p[child] = parent

    x_parent = set()
     
    while x!=p[x]:
        x_parent.add(p[x])
        x=p[x]
     
    while y!=p[y]:
        if p[y] in x_parent:
            break
        y=p[y]
     
    cnt=0
    for i in range(1,V+1):
        while i!=p[i]:
            if p[i]==p[y]:
                cnt+=1
                break
            i=p[i]
         
    print('#{} {} {}'.format(tc, p[y],cnt+1))