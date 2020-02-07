import sys
sys.stdin = open('input.txt')
# 0. 암호코드 정보 추출을 위한 dictionary 생성
password_code = {'0001101': 0, '0011001': 1, '0010011': 2,
                '0111101': 3, '0100011': 4, '0110001': 5,
                '0101111': 6, '0111011': 7, '0110111' : 8,
                '0001011': 9}
# 1. test data 입력
T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    
    # 2. 암호코드 추출
    for _ in range(N):
        line = input()
        for i in range(M-1, -1, -1): # 들어오는 배열마다, 뒤에서 부터 '1' 탐색
            if line[i] == '1':
                code = line[i-55:i+1] # 56자리 암호코드 추출
                break
    
    # 3. 암호코드 변환 및 분리 (7 x 8)
    result = []
    for i in range(8):
        result.append(password_code[code[7*i:7*i+7]])
    
    # 4. 암호코드 더하기
    answer = result[-1] # 검증코드 먼저 더하기
    for idx in range(7):
        if idx % 2:
            answer += result[idx] # 코드의 순서가 짝수 일때
        else:
            answer += result[idx] * 3 # 코드의 순서가 홀수 일때
    
    # 5. 결과물 검증 및 출력
    if answer % 10 == 0:
        print('#{} {}'.format(tc, sum(result)))
    else:
        print('#{} 0'.format(tc))