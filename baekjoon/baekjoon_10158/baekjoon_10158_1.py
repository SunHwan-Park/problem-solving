w, h = list(map(int, input().split()))
p, q = list(map(int, input().split()))
t = int(input())

t = t % (2*(max(w, h)))
d = [1, -1]

x_count = 0
i = 0
while x_count < t:
    x_count += 1
    p += d[i]
    if p in [w, 0]:
        i = abs(i-1)

y_count = 0
j = 0
while y_count < t:
    y_count += 1
    p += d[j]
    if q in [h, 0]:
        i = abs(j-1)

print(p, q)