def solution(prices):
    answer = [0 for _ in range(len(prices))]
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            if prices[j] >= prices[i]:
                count += 1
            else:
                count += 1
                break
        answer[i] += count
    return answer
# -------------------------------
# 강사님 코드
def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            count += 1
            if prices[i] > prices[j]:
                break
        answer.append(count)
    return answer

print(solution([1, 2, 3, 2, 3]))