import sys
sys.stdin = open('input2.txt')

# 0. 암호코드 정보 추출을 위한 dictionary 생성
password_code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111' : 8, '0001011': 9}

# 1. test data 입력
T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    final_result = 0

    # 2. 암호코드 추출
    for _ in range(N):
        line = bin(int(input(), 16))[2:]
        for i in range(len(line)-1, -1, -1): # 들어오는 배열마다, 뒤에서 부터 '1' 탐색
            if line[i] == '1':
                result = []
                k = 1
                while len(result) < 8:
                    if i+1-56*k >= 0:
                        code = line[i+1-56*k:i+1] # 56자리 암호코드 추출
                    else:
                        code = line[:i+1]
                    if len(code) % 56:
                        code = ((len(code)//56 + 1)*56 - len(code))*'0' + code
                    for j in range(8):
                        try:
                            temp = code[7*j:7*(j+1)]
                            revised_code = ''
                            for l in range(0, k*7, k):
                                revised_code += temp[l]
                            result.append(password_code[revised_code])
                        except:
                            result = []
                            k += 1 
                            break
                validation = result[-1] # 검증코드 먼저 더하기
                for idx in range(7):
                    if idx % 2:
                        validation += result[idx] # 코드의 순서가 짝수 일때
                    else:
                        validation += result[idx] * 3 # 코드의 순서가 홀수 일때
                if validation % 10 == 0:
                    final_result += sum(result)