import sys
sys.stdin = open('input.txt')

di=[1,0,-1,0]
dj=[0,1,0,-1]
 
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    room= [list(map(int,input().split())) for _ in range(N)]
    max_cnt=0
    min_start=N**2
    for i in range(N):
        for j in range(N):
            cnt=1
            start=room[i][j]
            while True:
                for k in range(4):
                    ni=i+di[k]
                    nj=j+dj[k]
                    if 0<=ni<N and 0<= nj < N and room[ni][nj]==room[i][j]+1:
                        i, j =ni, nj
                        cnt+=1
                        break
                else:
                    break
            if cnt>max_cnt:
                max_cnt=cnt
                min_start=start
            if cnt==max_cnt and min_start>start:
                min_start=start 
    print('#{} {} {}'.format(tc,min_start,max_cnt))