# 월말 평가 알고리즘 [문제2] - 희토류를 찾아라.

#1. text data 입력 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)] # 희토류 매장량 지도
    
    #2. 최대 매장량 산맥 찾기
    result = [] # 결과 후보
    for i in range(N):
        for j in range(N): # 각 지역을 순회하면서
            if D[i][j] > 0: # 만약 그 지역에 희토류가 있다면
                value = D[i][j] # 해당 지역 매장량
                count = 0 # 해당 산맥의 면적
                Q = [(i, j)] # queue
                while Q: # queue 안 요소가 다 소진될 때까지
                    ci, cj = Q.pop(0) # 현재 위치
                    D[ci][cj] = 0 # 현재 위치 매장량 지워주기
                    count += 1 # 해당 산맥 면적 추가
                    for k in range(-1, 2):
                        for l in range(-1, 2): # 주변 8방향을 확인하면서(본인 스스로는 매장량이 0이 되어서 자연스럽게 빠지게 된다.)
                            if 0 <= ci+k < N and 0 <= cj+l < N and D[ci+k][cj+l] == value and (ci+k, cj+l) not in Q:
                                # 지도 범위를 넘지 않으며, value가 같고, 현재 queue에 올라가 있지 않은 지역을 골라낸다.
                                Q.append((ci+k, cj+l))
                # 한 산맥의 매장량과 면적을 결과 후보에 등재
                result.append([value*count, count]) 

    #3. 결과 후보 중 조건에 맞는 산맥 찾기  
    result.sort(key=lambda x: x[1]) # 산맥 면적 기준으로 오름차순 정렬
    result.sort(key=lambda x: x[0], reverse=True) # 산맥 매장량 기준으로 내림차순 정렬

    #4. 결과 출력
    print('#{} {} {}'.format(tc, result[0][0], result[0][1]))