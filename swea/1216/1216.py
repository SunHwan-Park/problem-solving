import sys
sys.stdin = open('input.txt')

# 1216

# 0. 회문 검사 함수 생성
def palindrome(words):
    reversed_words = ''
    for char in words:
        reversed_words = char+reversed_words
    if reversed_words == words:
        return True
    else:
        return False

# 1. input data 입력(length, matrix)
for _ in range(10):
    t_num = int(input())
    m = []
    for _ in range(100):
        m.append(input())

    result = []
    # 2. 각 행에서 길이가 가장 긴 회문 찾기
    for row in range(100):
        for length in range(100, 0, -1): # 가장 긴 길이부터 탐색
            for i in range(100-length+1):
                if palindrome(m[row][i:i+length]):
                    result.append(length)
                    break
            if palindrome(m[row][i:i+length]):
                break

        # 3. 각 열에서 길이가 가장 긴 회문 찾기
        col_word = ''
        for col in range(100):
            col_word += m[col][row]
        for length in range(100, result[0], -1): # 가장 긴 길이부터 탐색(행에서 찾은 최대 회문 길이 이하로는 탐색 x)
            for i in range(100-length+1):
                if palindrome(col_word[i:i+length]):
                    result.append(length)
                    break
            if palindrome(col_word[i:i+length]):
                break
    
    # 4. 결과 출력
    print('#{} {}'.format(t_num, max(result)))