# 0. 판독기 함수 생성
def ginki(m, k, costumers):
    # 0_1. 각 초별 추가되는 빵 개수 리스트 생성
    breads = [0] # 0초는 0개
    for s in range(1, costumers[-1]+1):
        if s % m == 0: # m초의 배수가 되었을 때 k개의 빵이 추가됨.
            breads.append(k)
        else: # m초의 배수가 아닐 때는 빵이 추가되지 않음.
            breads.append(0)
    # 0_2. 
    for c in costumers:
        if sum(breads[:c+1]) < 1: # 현재 c초까지 남아있는 빵 개수의 합이 1개보다 작을 때
            return False
        else: # 현재 c초까지 남아있는 빵 개수가 1개 이상일 때(빵 개수를 하나 줄임)
            breads[c] -= 1
    return True

# 1. test data 입력
for test in range(int(input())):
    n, m, k = list(map(int, input().split()))
    costumers = sorted(list(map(int, input().split())))
    
    # 2. 판독기 실행 및 결과 출력
    if ginki(m, k, costumers):
        print('#{} Possible'.format(test+1))
    else:
        print('#{} Impossible'.format(test+1))