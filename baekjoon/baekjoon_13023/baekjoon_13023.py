import sys
N, M = map(int, sys.stdin.readline().split())
matrix = [[0 for _ in range(N)] for _ in range(N)]
near_list = {i:[] for i in range(N)}
for _ in range(M):
    p1, p2 = map(int, sys.stdin.readline().split())
    # 인접행렬
    matrix[p1][p2] = matrix[p2][p1] = 1
    # 인접리스트
    near_list[p1].append(p2)
    near_list[p2].append(p1)

answer = 0
for i in range(N):
    for j in set(near_list[i]) - set([i]):
        for k in set(near_list[j]) - set([i, j]):
            for l in set(near_list[k]) - set([i, j, k]):         
                if set(near_list[l]) - set([i, j, k, l]):
                    answer = 1
                    break
            if answer > 0:
                break
        if answer > 0:
            break
    if answer > 0:
        break

print(answer)


# ---------------------------
# # 강사님 코드
# import sys
# V, Edge = map(int, sys.stdin.readline().split())
# M = [[0 for _ in range(V)] for _ in range(V)]
# G = [[] for _ in range(V)]
# F = []

# for _ in range(Edge):
#     p1, p2 = map(int, sys.stdin.readline().split())
#     # 1. 인접행렬
#     M[p1][p2] = M[p2][p1] = 1
    
#     # 2. 인접 리스트
#     G[p1].append(p2)
#     G[p2].append(p1)

#     # 3. edge
#     F.append([p1, p2])
#     F.append([p2, p1])

# for i in range(len(F)):
#     for j in range(len(F)):
#         A, B = F[i]
#         C, D = F[j]

#         if A == B or A == C or A == D or B == C or B == D or C == D:
#             continue
#         if not M[B][C]:
#             continue
#         for E in G[D]:
#             if E == A or E == B or E == C or E == D:
#                 continue
#             print(1)
#             sys.exit(0)
            
# print(0)