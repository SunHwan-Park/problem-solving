data = []
k = int(input())
for _ in range(k):
    num = int(input())
    if num:
        data.append(num)
    else:
        data.pop()
print(sum(data))

# ----------------------
# 강사님 코드

stack = []
T = int(input())
for _ in range(T):
    num = int(input())
    if num:
        stack.append(num)
    else:
        if stack:
            stack.pop()
print(sum(stack))