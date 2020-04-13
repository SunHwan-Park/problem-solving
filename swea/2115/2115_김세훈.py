import sys
sys.stdin = open('input.txt')

def cal(temp):
    ret=0
    for i in range(1,1<<m):
        tsum=0
        ttsum=0
        for j in range(0,m):
            if i&(1<<j):
                tsum+=temp[j]
                ttsum+=temp[j]**2
        if tsum<=c and ret<ttsum:
            ret=ttsum
    return ret
 
for t in range(1,int(input())+1):
    n,m,c=list(map(int, input().split()))
    b=[[*map(int,input().split())]for _ in'a'*n]
 
    d=[]
    for i in b:
        for j in range(n-m+1):
            d.append(cal(i[j:j+m]))
        for j in range(n-m+1,n):
            d.append(0)
 
    ans=0
    for i in range(len(d)-m):
        for j in range(i+m,len(d)):
            ans=max(ans,d[i]+d[j])
    print("#%i"%t,ans)