w, h = list(map(int, input().split()))
p, q = list(map(int, input().split()))
t = int(input())

t_w = t % (2*w)
t_h = t % (2*h)

x_count = 0
d = 1
while x_count < t_w:
    x_count += 1
    p += d
    if p in [w, 0]:
        d *= -1

y_count = 0
d = 1
while y_count < t_h:
    y_count += 1
    q += d
    if q in [h, 0]:
        d *= -1

print(p, q)