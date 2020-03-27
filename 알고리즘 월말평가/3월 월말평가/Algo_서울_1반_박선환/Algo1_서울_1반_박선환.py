# 월말 평가 알고리즘 [문제1] - 숫자 이동

#1. text data 입력 
T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 이동 횟수(시간)
    A = list(map(int, input().split())) # 첫 배열

    #2. N번 만큼 숫자 이동 시행
    for _ in range(N): # 이동 횟수 N번 만큼 시행
        temp = [0]*10 # 임시 배열
        for i in range(10): # 배열 A를 순회하면서
            if abs(A[i]) >= 10: # 만약 그 수의 절대값이 10 이상이면
                if i == 0: # 맨 앞일 때
                    temp[i] += abs(A[i])//2 # 더이상 왼쪽으로 갈 곳이 없으므로 제자리에서 -(-abs(A[i])//2) 만큼
                    temp[i+1] += abs(A[i])//2 # 오른쪽 한 칸에 abs(A[i])//2 만큼 
                elif i == 9: # 맨 뒤일 때
                    temp[i] += -abs(A[i])//2 # 더이상 오른쪽으로 갈 곳이 없으므로 제자리에서 -(abs(A[i])//2) 만큼
                    temp[i-1] += -abs(A[i])//2 # 왼쪽 한 칸에 -abs(A[i])//2 만큼 
                else:
                    temp[i+1] += abs(A[i])//2 # 오른쪽 한 칸에 abs(A[i])//2 만큼
                    temp[i-1] += -abs(A[i])//2 # 왼쪽 한 칸에 -abs(A[i])//2 만큼
            else: # 수의 절대값이 10 미만이라면
                if A[i] < 0: # 음수일 때
                    if i == 0: # 맨 앞일 때
                        temp[i] += -A[i] # 더이상 왼쪽으로 갈 곳이 없으므로 제자리에서 부호만 바꿔주기
                    else:
                        temp[i-1] += A[i] # 왼쪽 한 칸에 A[i] 만큼
                elif A[i] > 0: # 양수일 때
                    if i == 9: # 맨 뒤일 때
                        temp[i] += -A[i] # 더이상 오른쪽으로 갈 곳이 없으므로 제자리에서 부호만 바꿔주기
                    else:
                        temp[i+1] += A[i] # 오른쪽 한 칸에 A[i] 만큼
        A = temp # 배열 A를 update
    
    #3. 결과 출력
    print('#{} {}'.format(tc, ' '.join(map(str, A))))