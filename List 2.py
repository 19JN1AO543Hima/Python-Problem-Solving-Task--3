def prime(n):

    if n <= 0:

        return "Not defined"
    
    elif n == 1:

        return "Not prime"
    
    for i in range(2, n):

        if n % i == 0:

            return "Not prime"
        
    return "Prime"

def list_prime(lst):

    prime_list = [ ]

    for i in lst:

        x = prime(i)

        if x == "Prime":

            prime_list.append(i)

    return prime_list

print(list_prime([10, 501, 22, 37, 100, 999, 87, 351]))