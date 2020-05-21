import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    answer = 0
    catch = 0
    queue = deque()
    queue.append((N, 0))
    visit = set([N])
 
    while True:
        current, cnt = queue.popleft()
        num1 = current + 1
        num2 = current - 1
        num3 = current * 2
        num4 = current - 10
        cnt += 1
        temp_nums = [num1, num2, num3, num4]
        for num in temp_nums:
            if num == M:
                catch = 1
                break
            else:
                if 0 < num <= 1000000 and num not in visit:
                    queue.append((num, cnt))
                    visit.add(num)
        if catch == 1:
            answer = cnt
            break
    print('#{} {}'.format(tc, answer))