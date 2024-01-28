input_list1 = [1, 2, 1, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]

print(list(set([x for i, x in enumerate(input_list1) if input_list1.count(x) > 1])))

input_list2 = [2, 2, 3, 5, 9, 1, 1, 7, 3, 5, 8, 8, 10, 7, 5]

print(list(set([x for i, x in enumerate(input_list2) if input_list2.count(x) > 1])))

input_list3 = [10, 20, 50, 20, 60, 10, 50, 20, 60, 30, 30, 50]

print(list(set([x for i, x in enumerate(input_list3) if input_list3.count(x) > 1])))