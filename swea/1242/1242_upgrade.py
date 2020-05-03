import sys
sys.stdin = open('input.txt')

password_code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111' : 8, '0001011': 9}
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    answer = 0
    lines = set()
    for _ in range(N):
        line = input()
        if line not in lines:
            lines.add(line)
    code_list = set()
    for line in lines:
        line = bin(int(line, 16))[2:].strip('0')
        while line:
            k = 1
            while True:
                result = []
                code = line[-56*k:]
                if len(code) % 56:
                    code = ((len(code)//56 + 1)*56 - len(code))*'0' + code
                for i in range(8):
                    sub_code = code[7*k*(i):7*k*(i+1)]
                    Rsub_code = ''
                    for j in range(0, k*7, k):
                        Rsub_code += sub_code[j]
                    try:
                        result.append(password_code[Rsub_code])
                    except:
                        k += 1
                        break
                else:
                    if code not in code_list:
                        code_list.add(code)
                        validation = result[-1]
                        for idx in range(7):
                            if idx % 2:
                                validation += result[idx]
                            else:
                                validation += result[idx] * 3
                        if validation % 10 == 0:
                            answer += sum(result)
                    line = line[:-56*k].strip('0')
                    break
    print('#{} {}'.format(tc, answer))