import numpy as np
# a = np.array([1,2,3])
# print(a)
# print(type(a))

# b = np.zeros((2,3), dtype=np.bool_)
# print(b)

# c = np.ones((2,5), dtype=np.uint8)
# print(c)

# d = np.array([[1,2], [2,4]])
# e = np.array([[4,5], [2,7]])
# c = d+e
# a = e.transpose()
# A = np.array([[1, 4, 5, 12], 
#               [-5, 8, 9, 0],
#               [-6, 7, 11, 19]])
# print(A[:,-1])




# 1: Convert two lists into a dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dist = dict(zip(keys,values))
# print(dist)


# 2: Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict4 = {'Sixty': 60, 'Seventy': 70}

# dict3 = dict1.copy()
# dict3.update(dict2)

# dict3 = {**dict1, **dict2}
# print(dict3)




# 3: Print the value of key ‘history’ from the below dict
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sampleDict['class']['student']['marks']['history'])




# 4: Initialize dictionary with default values
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# dist = dict()

# dist = dict.fromkeys(employees,defaults)
    
# print(dist)




# 5: Create a dictionary by extracting the keys from a given dictionary

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# keys = ["name", "salary"]
# res = dict()
# for k in keys:
#     res.update({k:sample_dict[k]})
# print(res)




# 6: Delete a list of keys from a dictionary
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# keys = ["name", "salary"]
# res = dict()
# for k in keys:
#     sample_dict.pop(k)
# print(sample_dict)



# 7: Check if a value exists in a dictionary

# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# if 200 in sample_dict.values():
#     print('200 is present in dict')
# print(sample_dict.get('b', '200 is present in a dict'))




# 8: Rename key of a dictionary

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# sample_dict['location'] = sample_dict.pop('city')
# print(sample_dict)





# 9: Get the key of a minimum value from the following dictionary
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': -75,
#   'history1': 751,
#   'history2': 705,
#   'history3': 175,
  
# }
# min = 9999999
# for key,value in sample_dict.items():
#     if value<min:
#         min = value
        
# print(min)



# 10: Change value of a key in a nested dictionary

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']['salary'] = 8500
print(sample_dict)