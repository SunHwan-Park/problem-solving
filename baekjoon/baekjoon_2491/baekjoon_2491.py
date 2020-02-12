n = int(input())
numbers = list(map(int, input().split()))

max_len = 1
temp_cre = [numbers[0]]
temp_dcre = [numbers[0]]
for i in range(1, n):
    if numbers[i] >= numbers[i-1]:
        temp_cre.append(numbers[i])
    else:
        if len(temp_cre) > max_len:
            max_len = len(temp_cre)
        temp_cre = [numbers[i]]
    if numbers[i] <= numbers[i-1]:
        temp_dcre.append(numbers[i])
    else:
        if len(temp_dcre) > max_len:
            max_len = len(temp_dcre)
        temp_dcre = [numbers[i]]
if len(temp_cre) > max_len:
    max_len = len(temp_cre)
if len(temp_dcre) > max_len:
    max_len = len(temp_dcre)

print(max_len)