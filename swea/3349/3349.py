import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    W, H, N = map(int, input().split())
    count = 0
    sx, sy = map(int, input().split())
    for _ in range(N-1):
        cx, cy = map(int, input().split())
        if (sx < cx and sy < cy) or (sx > cx and sy > cy):
            count += abs(cx - sx) + abs(cy - sy) - min(abs(cx - sx), abs(cy - sy))
        else:
            count += abs(cx - sx) + abs(cy - sy)
        sx, sy = cx, cy
    print('#{} {}'.format(tc, count))