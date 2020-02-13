import sys
sys.stdin = open('input.txt')

test_size = int(input())
for tc in range(test_size):
    sudoku = []
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))
        
    answer = 0
    
    for i in range(9):
        if set(sudoku[i]) != set(range(1,10)):
            answer += 1
        temp = []
        for j in range(9):
            temp.append(sudoku[j][i])
        if set(temp) != set(range(1,10)):
            answer += 1

    for i in range(3):
        for j in range(3):
            temp = []
            for k in range(3*i, 3*i+3):
                temp.extend(sudoku[k][3*j:3*j+3])
            if set(temp) != set(range(1, 10)):
                answer += 1

    if answer:
        print('#{} {}'.format(tc+1, 0))
    else:
        print('#{} {}'.format(tc+1, 1))