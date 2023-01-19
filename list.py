# 1. reverse a list
# list = [1,2,3,4,5]
# for i in list[4:0:-1]:
#     print(i)
# list[i] = list[::-1]

# list.reverse()
# print(list)




#  2: Concatenate two lists index-wise

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# ans = []
# ans = [i + j for i, j in zip(list1, list2)]
# print(ans)



# 3: square every element of list
# numbers = [1, 2, 3, 4, 5, 6, 7]
# res = []
# for i in numbers:
#     res.append(i**2)
# res2 = [i*i for i in numbers]
# print(res)
# print(res2)





# 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]

# ans = []
# for i in list1:
#     for j in list2:
#         ans.append(i+j)

# print(ans)





# 5: Iterate both lists simultaneously

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# res = []
# for x,y in zip(list1,list2[::1]):
#     print(x,y)






# 6: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# res = []
# for i in list1:
#     if(i!=""):
#         res.append(i)
# res2 = list(filter(None, list1))
# print(res2)




# 7: Add new item to list after a specified item

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)


# 8: Extend nested list by adding the sublist

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub_list = ["h", "i", "j"]
# list1[2][1][2].extend(sub_list)
# print(list1)




# 9: Replace list’s item with new value if found

# list1 = [5, 10, 15, 20, 25, 50, 20]
# index = list1.index(20)
# list1[index] = 200
# print(list1)
    


# 10: Remove all occurrences of a specific item from a list.

# list1 = [5, 20, 15, 20, 25, 50, 20]
# res = []
# for i in list1:
#     if i != 20:
#         res.append(i)
# for i in list1:
#     if i==20:   
#         list1.remove(20)
# print(list1)