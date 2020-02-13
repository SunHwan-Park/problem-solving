def solution(arrangement):
    answer = 0
    count = 0
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            if arrangement[i+1] == ')':
                answer += count
            else:
                count += 1
        else:
            if arrangement[i-1] == '(':
                pass
            else:
                count -= 1
                answer += 1
    
    return answer