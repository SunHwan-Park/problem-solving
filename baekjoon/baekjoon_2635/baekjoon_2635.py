n = int(input())

max_len = 0
for second in range(1, n+1):
    result = [n]
    result.append(second)
    next_num = n - second

    while next_num >= 0:
        result.append(next_num)
        next_num = result[-2] - result[-1]

    if len(result) > max_len:
        max_len = len(result)
        max_nums = result

print(max_len)
print(' '.join(map(str, max_nums)))