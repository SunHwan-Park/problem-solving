import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1 ,T+1):
    numbers, count = input().split()
    
    for _ in range(int(count)):
        temp = []
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                temp_num = numbers[:i]+numbers[j]+numbers[i+1:j]+numbers[i]+numbers[j+1:]
                temp.append(int(temp_num))
        numbers = str(max(temp))
    print('#{} {}'.format(tc, numbers))