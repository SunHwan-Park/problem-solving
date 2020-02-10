import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    V, E = list(map(int, input().split()))
    d = list(map(int, input().split()))
    arr = [d[2*i:2*i+2] for i in range(E)]
    leading = [arr[i][0] for i in range(len(arr))]
    trailing = [arr[i][1] for i in range(len(arr))]

    result = []
    max_count = 0
    for lead_num in leading:
        if leading.count(lead_num) > max_count:
            max_count = leading.count(lead_num)
            max_leading = lead_num
    result.append(max_leading)
    for i in arr:
        if i[0] == max_leading:
            arr.remove(i)
    leading = [arr[i][0] for i in range(len(arr))]
    trailing = [arr[i][1] for i in range(len(arr))]

    while len(arr) > 0:
        max_count = 0
        for lead_num in leading:
            if leading.count(lead_num) > max_count:
                max_count = leading.count(lead_num)
                max_leading = lead_num
    
        result.append(max_num)
        for i in arr:
            if i[0] == max_num:
                arr.remove(i)
        leading = [arr[i][0] for i in range(len(arr))]
        trailing = [arr[i][1] for i in range(len(arr))]
    for i in set(d) - set(result):
        result.append(i)
    
    print(result)
    