import sys
sys.stdin = open('input.txt')

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
for t in range(1, 11):
    length = int(input())
    m = []
    for _ in range(8):
        m.append(input())

    result = 0
    # 2. 각 행에서 회문 찾기
    for row in range(8):
        for i in range(8-length+1):
            if palindrome(m[row][i:i+length]):
                result += 1
        
        # 3. 각 열에서 회문 찾기
        col_word = ''
        for col in range(8):
            col_word += m[col][row]
        for i in range(8-length+1):
            if palindrome(col_word[i:i+length]):
                result += 1
    
    # 4. 결과 출력
    print('#{} {}'.format(t, result))