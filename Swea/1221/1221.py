import sys
sys.stdin = open('input.txt')

# 1221
strnum_dict = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
intnum_dict = {strnum_dict[key]:key for key in strnum_dict}

T = int(input())
for tc in range(1, T+1):
    t_num, N = input().split()
    numbers = [strnum_dict[num] for num in input().split()]
    numbers.sort()
    result = [intnum_dict[num] for num in numbers]
    
    print('#{}\n{}'.format(tc, ' '.join(result)))