import sys
sys.stdin = open('input.txt')

def f(lst):
    result = 0
    if set([8, 9, 0]).intersection(set(lst)) == set([8, 9, 0]):
        result = 1
    if set([1, 9, 0]).intersection(set(lst)) == set([1, 9, 0]):
        result = 1
    for n in set(lst):
        if lst.count(n) >= 3:
            result = 1
            break
    
    lst.sort()
    for i in range(len(lst)-2):
        temp = lst[i:i+3]
        if temp[1] == temp[0] + 1 and temp[2] == temp[0] + 2:
            result = 1
            break
    return result

T = int(input())
for tc in range(1, T+1):
    D = list(map(int, input().split()))
    P1 = D[0:3:2]
    P2 = D[1:4:2]
    answer = 0
    for i in range(2, 6):
        P1.append(D[2*i])
        P2.append(D[2*i+1])
        if f(P1):
            answer = 1
            break
        elif f(P2):
            answer = 2
            break
    print('#{} {}'.format(tc, answer))