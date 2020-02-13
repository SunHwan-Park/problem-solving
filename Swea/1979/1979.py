import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    puzzle = []
    for _ in range(N):
        puzzle.append(list(input().split()))
    
    result = 0
    # 각 행에 존재하는 빈칸 확인
    for i in range(N):
        for blank in ''.join(puzzle[i]).split('0'):
            if len(blank) == K:
                result += 1
        # 각 열에 존재하는 빈칸 확인                
        col = ''
        for j in range(N):
            col += puzzle[j][i]
        for blank in col.split('0'):
            if len(blank) == K:
                result += 1
            
    print('#{} {}'.format(tc, result))