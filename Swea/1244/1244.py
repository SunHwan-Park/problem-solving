import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1 ,T+1):
    number, count = input().split()
    numbers = [number]
    for _ in range(int(count)):
        for number in numbers:
            numbers.pop()
            temp = []
            for i in range(len(number)-1):
                for j in range(i+1, len(number)):
                    temp_num = number[:i]+number[j]+number[i+1:j]+number[i]+number[j+1:]
                    temp.append(int(temp_num))
            temp.sort()
        for _ in range(3):
            numbers.append(str(temp.pop()))

    print('#{} {}'.format(tc, max(numbers)))