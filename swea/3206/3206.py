import sys
sys.stdin = open('input.txt')

#1. 간단 버전...
T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    print('#{} {}'.format(tc, A+B))

#2. str 이용 버전
T = int(input())
for tc in range(1, T+1):
    answer = ''
    nums = input().split()
    nums.sort(key=lambda x: len(x))
    A, B = nums[0], nums[1]
    min_len = len(A)
    cal_num = str(int(B[-min_len:]) + int(A))

    while len(cal_num) != min_len:
        answer = cal_num[-min_len:] + answer
        B = B[:-min_len]
        A = cal_num[:-min_len]
        min_len = len(A)
        if len(B) > 0:
            cal_num = str(int(B[-min_len:]) + int(A))
        else:
            cal_num = A
    if len(B) > 0:
        B = B[:-min_len] + cal_num + answer
    else:
        B = cal_num + answer
        
    print('#{} {}'.format(tc, B))