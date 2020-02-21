import sys
sys.stdin = open('input.txt')

#1. test data 입력
T = int(input())
for tc in range(1 ,T+1):
    number, count = input().split()

    #2. 정해진 횟수만큼 카드 교환
    changed_num = []
    changed_idx = []
    for _ in range(int(count)): # 교환 시행
        probable = []
        for i in range(len(number)):
            for j in range(i+1, len(number)):
                if i != j:
                    # 현재 상태에서 1회 교환 시 가능한 모든 경우의
                    temp_num = number[:i]+number[j]+number[i+1:j]+number[i]+number[j+1:]
                    # 숫자 배열, 바꿔진(앞으로 당겨진) 수, 해당 수의 index 저장
                    probable.append([int(temp_num), number[j], j])

        probable.sort(key=lambda x: x[0])
        number = str(probable[-1][0]) # 가능한 숫자 배열들 중 가장 큰 수를 새로운 number로
        changed_num.append(probable[-1][1]) # 이번 시행에서 바꿔진 수 저장
        changed_idx.append(probable[-1][2]) # 이번 시행에서 바꿔진 수의 index 저장

    #3. 예외 상황 후처리(ex_32888->88823)
    number = list(number) # 교환이 모두 끝난 상태의 숫자배열 형변환
    
    r_nums = []
    for i in set(changed_num):
        if changed_num.count(i) > 1: # 바꿔진 수 중에서 중복이 있는 경우
            r_nums.append(i)

    # 중복이 있는 수의 idx 찾아내기
    for num in r_nums:
        idx = []
        for i in range(len(changed_num)):
            if changed_num[i] == num:
                idx.append(changed_idx[i])
        idx.sort()
        
        # 현재 number 해당 index에 있는 숫자들 찾아내기
        temp_num = []
        for i in idx:
            temp_num.append(number[i])
        temp_num.sort(reverse=True) # 내림차순 정렬

        # 해당 숫자들의 위치를 내림차순 정렬해준 상태로 변환
        for i in range(len(idx)):
            number[idx[i]] = temp_num[i]
    
    # 4. 결과 출력
    print('#{} {}'.format(tc, ''.join(number)))