import sys
sys.stdin = open('input.txt')

# 1. test data 입력
T = int(input())
for tc in range(1, T+1):
    text = input()
    H = int(input())
    hyphen_loc = list(map(int, input().split()))

    # 2. 각 hyphen 위치별 개수 세기
    hyphen_num = [0 for _ in range(len(text)+1)]
    for i in hyphen_loc:
        hyphen_num[i] += 1

    # 3. hyphen 추가
    count = 0 # '-'가 추가 됨에 따라, text의 인덱스가 달라지는 문제 커버하기 위한 변수 
    for loc in sorted(list(set(hyphen_loc))): # 각 hyphen 위치별 한 번씩만 시행
        text = text[:loc+count] + '-'*hyphen_num[loc] + text[loc+count:]
        count += hyphen_num[loc]
    
    # 4. 결과 출력
    print('#{} {}'.format(tc, text))

# ------------------------------------------
# 다른 사람 코드
# insert 쓰면 편했구나...ㅎㅎ
for t in range(int(input())):
    w=list(input())
    N=int(input())
    L=sorted(list(map(int,input().split())))
    for i in range(N):
        w.insert(L[i]+i,'-')
    print(f"#{t+1} {''.join(w)}")