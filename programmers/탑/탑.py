def solution(heights):
    answer = []
    for i in range(len(heights)):
        for j in range(i-1, -1, -1):
            if heights[j] > heights[i]:
                answer.append(j+1)
                break
        if len(answer) < i+1:
            answer.append(0)

    return answer
# ------------------------
# 강사님 코드
def solution(heights):
    answer = []
    for i in range(len(heights)):
        for j in range(i-1, -1, -1):
            if heights[j] > heights[i]:
                answer.append(j+1)
                break
        else: # 안 멈추고 다 돌면!
            answer.append(0)
    return answer
# --------------------------
# 스택 사용해서!
def solution(heights):
    answer = []
    for i in range(len(heights)):
        stack = []
        for j in range(i):
            if heights[j] > heights[i]:
                stack.append(j+1)
        if stack:
            answer.append(stack.pop())
        else:
            answer.append(0)
    return answer

print(solution([6,9,5,7,4]))