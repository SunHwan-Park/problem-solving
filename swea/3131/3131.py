N = 1000000
check_prime = [0, 0] + [1]*(N-1)
prime_nums = []

for num in range(2,  N+1):
    if check_prime[num]:
        prime_nums.append(num)
        for multiple_of_num in range(2*num, N+1, num):
            check_prime[multiple_of_num] = 0

print(' '.join(map(str, prime_nums)))