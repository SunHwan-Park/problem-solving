import sys
sys.stdin = open('input.txt')

# 1. test data 입력
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    hays = []
    for _ in range(N):
        hays.append(int(input()))
 
    # 2. 건초더미 크기를 동일하게 맞추는 데 필요한 횟수 구하기
    same_size = int(sum(hays) / len(hays)) # 원래 모든 건초더미의 크기
    count = 0
    for hay in hays:
        count += abs(same_size - hay)
    count //= 2
    
    # 3. 결과 출력
    print('#{} {}'.format(tc, count))