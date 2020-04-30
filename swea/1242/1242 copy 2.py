import sys
sys.stdin = open('input.txt')

# 0. 암호코드 정보 추출을 위한 dictionary 생성
password_code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111' : 8, '0001011': 9}

# 1. test data 입력
T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    answer = 0
    possible = set()
    # 2. 암호코드 추출
    lines = set()
    for _ in range(N):
        line = bin(int(input(), 16))[2:].strip('0')
        if line not in lines:
            lines.add(line)
            while line:    
                k = 1
                while True:
                    endcode = line[-14*k:]
                    revised_endcode1 = ''
                    revised_endcode2 = ''
                    for i in range(0, k*7, k):
                        revised_endcode1 += endcode[i]
                        revised_endcode2 += endcode[i+7*k]
                    try:
                        password_code[revised_endcode1]
                        password_code[revised_endcode2]
                        if len(line) >= 56*k:
                            possible.add(line[-56*k:])
                            line = line[:-56*k].strip('0')
                            k = 1
                        else:
                            possible.add(line)
                            line = ''
                        break
                    except:
                        k += 1

    for code in possible:
        if len(code) % 56:
            code = ((len(code)//56 + 1)*56 - len(code))*'0' + code
        result = []
        k = len(code)//56
        for i in range(8):
            revised_code = ''
            temp = code[7*i*k:7*(i+1)*k]
            for j in range(0, k*7, k):
                revised_code += temp[j]
            result.append(password_code[revised_code])
        validation = result[-1] # 검증코드 먼저 더하기
        for idx in range(7):
            if idx % 2:
                validation += result[idx] # 코드의 순서가 짝수 일때
            else:
                validation += result[idx] * 3 # 코드의 순서가 홀수 일때
        if validation % 10 == 0:
            answer += sum(result)
    
    print('#{} {}'.format(tc, answer))