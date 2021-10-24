list1 = [[(1, 2), (2,7)], [(3, 5), (18, 12)], [(9, 2), (9, 7)]]

print("Original list is : " + str(list1))

temp1 = [ele for sub in list1 for ele in sub]

res1 = list(zip(*temp1))

print("Converted tuple list : " + str(res1))
