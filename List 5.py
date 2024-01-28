def binomial_coefficient(N, M):

    res = 1

    if M > N - M:

        M = N - M

    for i in range(0, M):

        res *= (N - i)

        res /= (i + 1)

    return res

def calculate_ways(M, N):

    if M < N:

        return 0
    
    ways = binomial_coefficient(N + M - 1, N - 1)

    return int(ways)

if __name__ == '__main__':

 M = 7 ; N = 5

result = calculate_ways(M, N)

print(result)