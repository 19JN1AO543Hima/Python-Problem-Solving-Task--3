def subList(lst, l):

    for i in range(l - 1):

        s = lst[i]

        for j in range(i + 1, l):

            s += lst[j]

            if s == 0:

                return True
    
    return False
            
list = [4, 2, -3, 1, 6]

print(subList(list, len(list)))
