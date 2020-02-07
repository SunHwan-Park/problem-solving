import sys
sys.stdin = open('input.txt')

# 1. 적당히 큰 정수에 해당하는 좌표 정보 생성
num_location = {}
num_count = 0
for i in range(1, 284):
    for j in range(1, i+1):
        num_count += 1
        num_location[num_count] = (j, i + 1 - j)
r_num_location = {loc:num for num, loc in num_location.items()} # num_location의 key, value가 뒤집힌 형태

# 2. test data 입력
T = int(input())
for tc in range(1, T+1):
    p, q = list(map(int, input().split()))
    # 3. &(p)+&(q) 구하기
    target_loc = (num_location[p][0] + num_location[q][0], num_location[p][1] + num_location[q][1])
    # 4. #(&(p)+&(q)) 구하기
    answer = r_num_location[target_loc]
    # 5. 결과 출력
    print('#{} {}'.format(tc, answer))