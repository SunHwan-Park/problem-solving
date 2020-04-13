import sys
sys.stdin = open('input.txt')

def dfs(L,s) : 
    if visited[L][s] == True : 
        return
     
    if L == N : 
        visited[L][s] = True
        return
    else : 
        visited[L][s] = True    
        dfs(L+1,s+quiz[L])
        dfs(L+1,s)
 
T = int(input())
for t in range(1, 1+T) :
  
    N = int(input())
    quiz = list(map(int, input().split()))
    visited = [[False]*(100*N) for _ in range(N+1)]
    dfs(0,0)
    print(f'#{t} {sum(visited[N])}')