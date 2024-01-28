def first_non_repeated_el(list):

    ctr = {}

    for i in list:

        if i in ctr:

            ctr[i] += 1

        else:

            ctr[i] = 1

    for i in list:

        if ctr[i] == 1:

            return i
        
nums = [1, 2, 3, 1, 2, 4, 5, 6, 7, 8]

print("\nGiven list: ")

print(nums)

result = first_non_repeated_el(nums)

print("First non-repeated element in the given list: ")

print(result)

