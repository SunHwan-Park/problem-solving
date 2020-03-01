import sys
sys.stdin = open('input.txt')

#1. test data 입력
T = int(input())
for tc in range(1, T+1):
    day, month, t_month, year = map(int, input().split())
    plan = list(map(int, input().split()))

    #2. 최적 이용요금 계산
    best_plan = []
    
    #2_1. 매달 유리한 요금 찾기(일별, 월별)
    for m in range(12):
        if plan[m] > 0:
            if plan[m]*day > month: # 월별이 유리
                best_plan.append(month)
            else: # 일별이 유리
                best_plan.append(plan[m]*day)
        else: # 해당 달의 이용 계획이 없는 경우
            best_plan.append(0)
    
    #2_2. 3달 이용권이 유리한 경우 찾기1
    result = 0
    best_plan1 = best_plan[:]
    for _ in range(4):
        psb = [-500, -500]
        for m in range(10): # 10월까지
            if best_plan1[m] > 0:
                if sum(best_plan1[m:m+3]) > t_month:
                    if sum(best_plan1[m:m+3]) - t_month > psb[1]:
                        psb = [m, sum(best_plan1[m:m+3]) - t_month]
        try:
            best_plan1[psb[0]] = 0
            best_plan1[psb[0]+1] = 0
            best_plan1[psb[0]+2] = 0
            result += t_month
        except:
            pass

    if best_plan1[10] > 0: # 11월의 경우
        if sum(best_plan1[10:]) > t_month:
            best_plan1[10] = t_month
            best_plan1[11] = 0
    if best_plan1[11] > t_month: # 12월의 경우
        best_plan1[11] = t_month

    plan1 = result + sum(best_plan1)

    #2_3. 3달 이용권이 유리한 경우 찾기2
    best_plan2 = best_plan[:]
    for m in range(10): # 10월까지
        if best_plan2[m] > 0:
            if sum(best_plan2[m:m+3]) > t_month:
                best_plan2[m] = t_month
                best_plan2[m+1] = 0
                best_plan2[m+2] = 0
    if best_plan2[10] > 0: # 11월의 경우
        if sum(best_plan2[10:]) > t_month:
            best_plan2[10] = t_month
            best_plan2[11] = 0
    if best_plan2[11] > t_month: # 12월의 경우
        best_plan2[11] = t_month

    plan2 = sum(best_plan2)

    # 3. 비교하고 결과 출력
    print('#{} {}'.format(tc, min(year, plan1, plan2)))