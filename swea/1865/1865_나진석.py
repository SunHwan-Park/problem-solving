import sys
sys.stdin = open('input.txt')

def toSet(num):
    return { idx for idx, val in enumerate(bin(num)[:1:-1]) if val == '1' }
  
T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
     
    ans = [1] + [0]*((1<<N) - 1)
    size = [bin(i).count('1') for i in range(1<<N)]
    for R in range(N):
        for i in range(1<<N):
            if size[i] == R+1:
                ans[i] = max([ arr[R][C] * ans[i & ~(1<<C)] for C in toSet(i) ])
 
    print('#{} {:.6f}'.format(test, ans[-1]*100))