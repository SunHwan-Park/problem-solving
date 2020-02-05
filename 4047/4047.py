import sys
sys.stdin = open('input.txt')

# 1. test data 입력
T = int(input())
for tc in range(1, T+1):
    d = input()
    # 2_1. 현재 가지고 있는 카드의 리스트 생성
    cards = [d[3*i:3*i+3] for i in range(len(d) // 3)]
    # 2_2. 전체 카드 셋 생성
    full_cards = [char+'0'+str(num) if len(str(num))==1 else char+str(num) for num in range(1, 14) for char in ['S', 'D', 'H', 'C']]

    # 3. 모양별 부족한 카드 수 확인
    if len(cards) - len(set(cards)): # 중복된 카드가 있는 경우
        result = 'ERROR'
    else:
        S, D, H, C = 0, 0, 0, 0
        for card_needed in set(full_cards) - set(cards):
            if card_needed[0] == 'S':
                S += 1
            elif card_needed[0] == 'D':
                D += 1
            elif card_needed[0] == 'H':
                H += 1
            else:
                C += 1
        result = ' '.join(map(str, [S, D, H, C]))
    
    # 4. 결과물 출력
    print('#{} {}'.format(tc, result))