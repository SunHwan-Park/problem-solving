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

# # ---------------------------------------
# # 김태우 코드
# def solution(arrangement):
#     answer = 0
#     stack = 0
#     for index, i in enumerate(arrangement):
#         if i == ')' :
#             stack -= 1
#             if arrangement[index-1] == ')':
#                 answer += 1
#             else:
#                 answer += stack
#         else:
#             stack += 1
#     return answer

print(solution('()(((()())(())()))(())'))