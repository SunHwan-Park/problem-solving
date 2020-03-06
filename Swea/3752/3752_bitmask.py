import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    d = input()
    data = map(int,input().split())
    a = 1
    for i in data:
        a |= a<<i
    print('#%i'%tc, bin(a).count('1'))