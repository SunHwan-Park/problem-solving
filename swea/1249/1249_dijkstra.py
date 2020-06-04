import sys
sys.stdin = open('input.txt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, list(input()))) for _ in range(N)]
    dist = [[float('inf')]*N for _ in range(N)]
    V = [[0]*N for _ in range(N)]

    dist[0][0] = 0

    import heapq
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (dist[0][0], 0, 0))

    while heap:
        C = heapq.heappop(heap)
        if C[1] == N-1 and C[2] == N-1:
            break
        V[C[1]][C[2]] = 1
        for i in range(4):
            nx = dx[i] + C[1]
            ny = dy[i] + C[2]
            if 0 <= nx < N and 0 <= ny < N and V[nx][ny] == 0:
                if dist[nx][ny] > dist[C[1]][C[2]] + M[nx][ny]:
                    dist[nx][ny] = dist[C[1]][C[2]] + M[nx][ny]
                    heapq.heappush(heap, (dist[nx][ny], nx, ny))

    print('#{} {}'.format(tc, dist[N-1][N-1]))