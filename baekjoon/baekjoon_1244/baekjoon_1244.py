# 1. test data 입력
S = int(input())
d = list(map(int, input().split()))
n = int(input())
for _ in range(n):
    student = list(map(int, input().split()))

    # 2. 학생의 성별에 따라 스위치 변경
    if student[0] == 1: # 남학생일때
        for idx, switch in enumerate(d):
            if (idx + 1) % student[1] == 0:
                d[idx] = abs(d[idx] - 1)
    else: # 여학생일때
        d[student[1] - 1] = abs(d[student[1] - 1] - 1) # 처음 자리 스위치 변경
        for i in range(1, student[1]):
            try:
                if d[student[1] -1 - i] == d[student[1] -1 + i]:
                    d[student[1] - 1 - i] = abs(d[student[1] - 1 - i] - 1)
                    d[student[1] - 1 + i] = abs(d[student[1] - 1 + i] - 1)
                else:
                    break
            except:
                break # 한쪽 끝까지 탐색을 마쳤을 때

# 3. 결과 출력
for i in range(len(d)//20 + 1):
    print(' '.join(map(str, d[20*i:20*i+20])))