list = [10, 501, 22, 37, 100, 999, 87, 351]

listOdd = []

listEven = []

for num in list:

    if num % 2 == 0:

        listEven.append( num )

    else:

        listOdd.append( num )

print("list:  ",list)

print("listEven:  ",listEven)

print("listOdd:  ",listOdd)

