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