import sys
sys.stdin = open('input.txt')

# # 풀이 1(greedy)
# T = int(input())
# for tc in range(1, T+1):
#     d = list(map(int, input().split()))
#     result = []
#     for i in d:
#         for j in set(d) - set([i]):
#             for k in set(d) - set([i, j]):
#                 result.append(i + j + k)
#     result = sorted(list(set(result)))
#     print('#{} {}'.format(tc, result[-5]))

# # 풀이2(itertools)
# from itertools import combinations
# T = int(input())
# for tc in range(1, T+1):
#     d = list(map(int, input().split()))
#     result = []
#     for c in combinations(d, 3):
#         result.append(sum(c))
#     result = sorted(list(set(result)))
#     print('#{} {}'.format(tc, result[-5]))

# 풀이3(bit 연산)
T = int(input())
for tc in range(1, T+1):
    d = list(map(int, input().split()))
    result = []

    for i in range(1<<len(d)): # 1<<n : 부분 집합의 
        temp = []
        for j in range(len(d)+1): # 원소의 수만큼 비트
            if i & (1<<j): # i의 j번째 비트가 1
                temp.append((d[j]))
        if len(temp) == 3:
            result.append(sum(temp))

    result = sorted(list(set(result)))
    print('#{} {}'.format(tc, result[-5]))