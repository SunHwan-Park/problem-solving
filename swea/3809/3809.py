import sys
sys.stdin = open('input.txt')

#1. test data 입력
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    D = input().split()
    while len(D) != N:
        D.extend(input().split())

    #2. 가능한 모든 수 찾기
    answer = -1
    a = 0
    for i in range(1, N+1):
        probable = []
        for j in range(N - i + 1):
            probable.append(int(''.join(D[j:j+i])))

        #3. probable에 없는 수 중에서 가장 작은 정수 찾기
        probable = sorted(list(set(probable))) # 중복 제거, 오름차순 정렬
        probable = [p for p in probable if a <= p < 10**i] # 해당 자리수에 맞는 수만 골라내기
        for p in probable:
            if a < p and a not in probable:
                answer = a
                break
            else:
                a += 1
        if answer >= 0: # 정답이 나왔으면 멈추기
            break

    #4. 결과 출력
    print('#{} {}'.format(tc, answer))