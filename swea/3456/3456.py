import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T+1):
#     numbers = list(map(int, input().split()))
#     print('#{} {}'.format(tc, abs(sum(set(numbers))*2 - sum(numbers))))

for t in range(int(input())):
    d = list(map(int, input().split()))
    print('#{} {}'.format(t+1, abs(sum(set(d))*2 - sum(d))))