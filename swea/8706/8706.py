import sys
sys.stdin = open('input.txt')

# 1. test data 입력
T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    carrots = list(map(int, input().split()))

    # 2. 이동한 거리 계산
    distance = 0 # 이동한 거리
    current_loc = 0 # 현재 수레의 위치
    cart = 0 # 수레가 담고 있는 당근의 양
    i = 0 # 작업해야할 저장소

    while i != N: # 마지막 저장소까지 수행
        distance += (i+1) - current_loc # 현재 위치에서 해당 저장소로 도달하는 데 필요한 거리
        if carrots[i] >= M - cart: # 이번 저장소에서 수레가 꽉 찬다면
            carrots[i] -= M - cart # 해당 저장소에서 수레에 담는 당근 개수만큼 빼주고
            distance += (i+1) # 되돌아가는 거리를 추가
            current_loc = 0 # 첫위치로 리셋
            cart = 0 # 카트 비우기
        else: # 이번 저장소에서 수레가 꽉 차지 않는다면
            cart += carrots[i] # 수레에 해당 저장소의 당근을 다 더하고
            carrots[i] = 0 # 해당 저장소를 비움
            i += 1 # 다음 저장소를 목표로
            current_loc = i # 현재 위치 수정
    distance += N # 마지막 저장소에서 첫 위치로 돌아오는 데 필요한 거리
    
    # 3. 결과 출력
    print('#{} {}'.format(tc, distance))