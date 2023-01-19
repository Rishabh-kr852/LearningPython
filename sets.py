# 1: Add a list of elements to a set 

# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]

# for i in sample_list:
#     sample_set.add(i)
# print(sample_set)


# 2: Return a new set of identical items from two sets 

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set3 = set1.intersection(set2)
# print(set3)



# 3: Get Only unique items from two sets 

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# set3 = set1.union(set2)
# print(set3)



# 4: Update the first set with items that don’t exist in the second set 

# set1 = {10, 20, 30}
# set2 = {20, 40, 50}

# set1 = set1.difference(set2)
# print(set1)


# 5: Remove items from the set at once
# set1 = {10, 20, 30, 40, 50}
# set1.difference_update({10,20,30})
# print(set1)




# 6: Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# set3 = set1.symmetric_difference(set2)
# print(set3)



# 7: Check if two sets have any elements in common. If yes, display the common elements
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}

# set3 = set1.intersection(set2)
# if set3 is None:
#     print("No common element")
# else:
#     print(set3)




# 8: Update set1 by adding items from set2, except common items

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set1.symmetric_difference_update(set2)
# print(set1)



#  9: Remove items from set1 that are not common to both set1 and set2

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set1.intersection_update(set2)
# print(set1)


a = 'cy'
b = 'cy'
# print(id(a))
# print((id(b)))
print(a is b)
print(a == b)