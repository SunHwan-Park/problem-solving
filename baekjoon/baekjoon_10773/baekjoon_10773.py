data = []
k = int(input())
for _ in range(k):
    num = int(input())
    if num:
        data.append(num)
    else:
        data.pop()
print(sum(data))