code = '00011010001011010001101101110110111001001101000110111101'
'          11010001011010001101101110110111001001101000110111101'
password_code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111' : 8, '0001011': 9}


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
    print(sum(result))
else:
    print('0')