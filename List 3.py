l1 = [10, 501, 22, 37, 100, 999, 87, 351]

l2 = [ ]

def is_happy(l1):

    for i in range(len(l1)):
        
        sum = l1[i]

        while sum!= 1 and sum!= 4:

            tempsum = 0

            for digit in str(sum):

                tempsum += int(digit) **2
                
            sum = tempsum

        if sum == 1:

            l2.append(l1[i])

    return l2

print(is_happy(l1))