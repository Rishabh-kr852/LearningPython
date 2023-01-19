# import pdb

# class testing:

#     def __init__(self, *args):
#         print('Name is {}'.format(*args))
        
#     def display(*args):
#         print(*args)

# pdb.set_trace()
# name = testing()
# testing.display('word','hello', 'number')

# # import pandas
# # print(pandas.__version__)


def square(x):
	return x**2

i = [1,2,3,4,5]
# ans = map(square, i)
print(list(map(lambda x:x**2, i)))


# for using reduce in python 3 we need to import functools. It takes function, sequence as input and returns value as output
import functools
functools.reduce()