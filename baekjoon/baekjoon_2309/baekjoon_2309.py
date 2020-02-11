arr = [int(input()) for _ in range(9)]
over = sum(arr) - 100
two_short = []
for i in range(9):
    for j in range(9):
        if j != i:
            if arr[i] + arr[j] == over:
                two_short = [arr[i], arr[j]]
                break
    if two_short:
        break
result = sorted(list(set(arr) - set(two_short)))
for short in result:
    print(short)