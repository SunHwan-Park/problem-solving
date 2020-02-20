import sys
N, M, D = map(int, sys.stdin.readline().split())
enemy = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = []
for i in range(M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            s1 = i
            s2 = j
            s3 = k

            temp = enemy[:]
            count = 0
            for _ in range(N):
                for s in [s1, s2, s3]:
                    for i in range()