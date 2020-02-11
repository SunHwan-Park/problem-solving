bingo = []
for _ in range(5):
    bingo.append(list(map(int, input().split())))
numbers = []
for _ in range(5):
    numbers.extend(list(map(int, input().split())))

count = 0
for num in numbers:
    count += 1
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == num:
                bingo[i][j] = 0
    
    bingo_num = 0
    diagonal_1 = 0
    diagonal_2 = 0
    for i in range(5):
        if sum(bingo[i]) == 0:
            bingo_num += 1
        vertical = 0
        for j in range(5):
            vertical += bingo[j][i]
        if vertical == 0:
            bingo_num += 1
        diagonal_1 += bingo[i][i]
        diagonal_2 += bingo[i][4-i]
    if diagonal_1 == 0:
        bingo_num += 1
    if diagonal_2 == 0:
        bingo_num += 1

    if bingo_num >= 3:
        break

print(count)