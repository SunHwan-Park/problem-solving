import sys
sys.stdin = open('input.txt')

T = int(input())
result = [0]*T
def min_fee(month, fee):
    global total
    if month > 12:
        if total > fee:
            total = fee
    else:
        for i in range(3):
            if i == 0:
                min_fee(month +periods[i], fee + (fees[i]*infos[month]))
            else:
                min_fee(month +periods[i], fee + fees[i])
for t in range(T):
    fees = list(map(int, input().split()))
    infos = [0] + list(map(int, input().split()))
    periods = [1,1,3]
    total = fees[3]
    min_fee(1,0)
    result[t] = total
for r in range(T):
    print('#{} {}'.format(r+1, result[r]))