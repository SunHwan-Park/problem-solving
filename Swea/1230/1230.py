import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    command_N = int(input())
    commands = input().split()

    for i in range(len(commands)):
        if commands[i] == 'I':
            index = int(commands[i+1])
            nums_n = int(commands[i+2])
            for k in range(nums_n):
                numbers.insert(index+k, int(commands[i+3+k]))
        if commands[i] == 'D':
            index = int(commands[i+1])
            del_n = int(commands[i+2])
            for _ in range(del_n):
                del numbers[index]
        if commands[i] == 'A':
            add_n = int(commands[i+1])
            for k in range(add_n):
                numbers.append(int(commands[i+2+k]))
    print('#{} {}'.format(tc, ' '.join(map(str, numbers[:10]))))