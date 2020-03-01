import sys
sys.stdin = open('input.txt')

for t in range(int(input())):
    a,b,c,d=map(int, input().split());p=[*map(int, input().split())];q=[0]*13;r=[0]*13
    for i in range(12):
        if p[i]*a >b:q[i+1]=q[i]+b
        else:q[i+1]=q[i]+a*p[i]
    r[:3]=q[:3]
    for i in range(2, 12):r[i+1]=min(q[i+1],r[i-2]+c,r[i]+q[i+1]-q[i])
    print('#%d %d'%(t+1,min(d,r[-1])))