w, h = list(map(int, input().split()))
p, q = list(map(int, input().split()))
t = int(input())

count = 0
dx = [1, -1]
dy = [1, -1]
i = 0
j = 0
x, y = p, q
while count < t:
    count += 1
    d = [dx[i], dy[j]]
    x += d[0]
    y += d[1]

    if x in [w, 0]:
        i = abs(i-1)
    if y in [h, 0]:
        j = abs(j-1)

    if x == p and y == q and (i, j) == (0, 0):
        roof = count
        count = (t // roof)*roof
print(x, y)