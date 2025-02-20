import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = []
    for i in range(N-1):
        for j in range(i+1, N):
            temp = str(numbers[i]*numbers[j])
            count = 0
            for k in range(len(temp)-1):
                if temp[k] <= temp[k+1]:
                    count += 1
            if count == len(temp)-1 and count != 0:
                result.append(int(temp))
    
    if result:
        answer = max(result)
    else:
        answer = -1
    print('#{} {}'.format(tc, answer))

# ---------------------------------
# 강사님 코드_단조증가 구별 함수 활용
import sys
sys.stdin = open('input.txt')

def check(n):
    n, r = n // 10, n % 10
    while n != 0:
        if n % 10 > r:
            return False
        n, r = n // 10, n % 10
    
    return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = -1

    for i in range(N-1):
        for j in range(i+1, N):
            num = numbers[i] * numbers[j]
            if check(num) and result < num:
                result = num

    print('#{} {}'.format(tc, result))

# ------------------------------------------
# 김태우님 코드
T = int(input())
 
for t in range(1, T+1):
    n = int(input())
    ns = list(map(int, input().split()))
 
    max_result = 0
    for i in range(n):
        for j in range(i+1, n):
            m = ns[i] * ns[j]
            tmp = m
            if tmp >= 10:
                flag = True
                while tmp > 0:
                    tmp, r = divmod(tmp, 10) # 지렸다...
                    if not tmp % 10 <= r:
                        flag = False
                        break
                if flag:
                    if m > max_result:
                        max_result = m
 
    if max_result == 0:
        print("#{} {}".format(t, -1))
    else:
        print("#{} {}".format(t, max_result))