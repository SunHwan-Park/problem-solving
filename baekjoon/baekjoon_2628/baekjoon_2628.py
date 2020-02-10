l, b = list(map(int, input().split()))
n = int(input())
data = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])
length = '1'*l
breadth = '1'*b
l_count = 0
b_count = 0
for d in data:
    if d[0] == 0:
        breadth = breadth[:d[1]+b_count] + '0' + breadth[d[1]+b_count:]
        b_count += 1
    else:
        length = length[:d[1]+l_count] + '0' + length[d[1]+l_count:]
        l_count += 1

print(max([len(l) for l in length.split('0')]) * max([len(b) for b in breadth.split('0')]))