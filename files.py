


# Reading from an existing file 
# with open('test.txt', 'r') as f:
#     # for l in f:
#     #     print(l, end='')
    
#     # print(f.read())
#     # print(f.readline(), end='')
#     # print(f.readlines(), end='')
    
#     size_to_read = 10
#     f_contents = f.read(size_to_read)
#     print(f_contents)
#     f.seek(2)
#     f_contents = f.read(size_to_read)
#     print(f_contents)
    
    
#     print(f.tell())
    # while len(f_contents) > 0:
    #     print(f_contents)
    #     f_contents = f.read(size_to_read)
        
# Creating/Writing in a file 
# with open('test1.txt','w') as f:
#     f.write('Hello')


# Reading and writing simultaneously for multiple files
# with open('test.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for lines in rf:
#             wf.write(lines)
    
# In order to work with images consider writing the mode with as 'rb' or 'wb' which will done in binary mode    


# import os
# print(os.getcwd())



# import sys
# def whatever():
#     try:
#         f = open ( "foo.txt", 'r' )
#     except IOError as Error:
#         print(Error)
#         print(sys.exc_type)
# whatever()