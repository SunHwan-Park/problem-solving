import sys
sys.stdin = open('input.txt')

T= int(input())
for tc in range(1,T+1):
    N= int(input())
    arr = list(map(int,input().split()))
    position = [(arr[2*i], arr[2*i+1]) for i in range(N+2)]
    visited=1
 
    dist = [[0]*(N+2) for _ in range(N+2)]
    cache = [[200*(N+1)] * (2**(N+2)) for _ in range(N+2)]
    cache[0][1]=0
 
    def f(now, visited):
        if visited==2**(N+2)-1-2:
            if dist[now][1]==0:
                dist[now][1]=abs(position[now][0]-position[1][0])+abs(position[now][1]-position[1][1])
 
            if cache[now][visited]+dist[now][1]<cache[1][visited|(1<<1)]:
                cache[1][visited|(1<<1)]=cache[now][visited]+dist[now][1]
 
        else:
            for i in range(2,N+2):
                if ( 1 << i ) & visited==0:
                    if dist[now][i]==0:
                        dist[now][i]=abs(position[i][0]-position[now][0])+abs(position[i][1]-position[now][1])
 
                    if cache[now][visited]+dist[now][i] < cache[i][visited|(1<<i)]:                 
                        cache[i][visited|(1<<i)]=cache[now][visited]+dist[now][i]
                        f(i, visited|(1<<i))
      
    f(0,1)
    all_visited=2**(N+2)-1
    print('#{} {}'.format(tc, cache[1][all_visited]))