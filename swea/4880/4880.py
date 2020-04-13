def rcp(A, B, point): # 가위바위보 함수
    if [A[0], B[0]] in [[2, 1], [3, 2], [1, 3], [1, 1], [2, 2], [3, 3]]: # 앞쪽이 이겼을 경우
        return A # 그대로 결과를 올려보낸다
    else: # 뒷쪽이 이겼을 경우
        return [B[0], B[1]+point] # 현재 까지 쌓아올린 index에다가, point 값을 더해준다

def game(li): # game 함수
    if len(li) == 1: # 한 개까지 나눠졌을 때
        index = 1
        return [li[0], index]
    else: # 나눌 것이 있을 때
        point = (1 + len(li)) // 2
        li1 = li[:point]
        li2 = li[point:]
        return rcp(game(li1), game(li2), point)

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    result = game(cards)
    print('#{} {}'.format(tc, result[1]))