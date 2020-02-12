n = int(input())
for _ in range(n):
    A = list(map(int, input().split()))[1:]
    B = list(map(int, input().split()))[1:]
    A_1 = A.count(1)
    A_2 = A.count(2)
    A_3 = A.count(3)
    A_4 = A.count(4)
    B_1 = B.count(1)
    B_2 = B.count(2)
    B_3 = B.count(3)
    B_4 = B.count(4)

    if A_4 != B_4:
        if A_4 > B_4:
            print('A')
        else:
            print('B')
    elif A_3 != B_3:
        if A_3 > B_3:
            print('A')
        else:
            print('B')
    elif A_2 != B_2:
        if A_2 > B_2:
            print('A')
        else:
            print('B')
    elif A_1 != B_1:
        if A_1 > B_1:
            print('A')
        else:
            print('B')
    else:
        print('D')