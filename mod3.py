# i=1
# while i<6:
#     print(i)
#     i+=1
    



# 2: Print the following pattern

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# row = 5
# for i in range(1, row + 1, 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print("")


# x = int(input("enter a number : "))
# res = 0
# for i in range(1,x+1,1):
#     res += int(i)
# print(res)


# x = 2
# ans = 1
# for i in range(1,10,1):
#     ans = x*i
#     print(ans)



# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i%5 == 0:
#         print(i)


# x = 76543
# count = 0
# while x>0:
#     x = x // 10
#     count += 1
# print(x)
# print(count)


# for i in range(-10,0,1):
#     print(i)


# start = 25
# end = 50

# for i in range(25,end+1):
#     if i>1:
#         for j in range(2,i):
#             if i%j == 0:
#                 break
#         else:
#             print(i)


# r = 5
# for i in range(1,(2*r)+1):
#     if i <= r:
#         for j in range(1,i+1):
#             print("*", end=' ')
#         print("")
#     # else:
#     #     for j in range(1,i-(2*j),1):
#     #         print("*", end=' ')
#     #     print("")
# for i in range(r,1,-1):
#     for j in range(0,i-1):
#         print("*", end=' ')
#     print("")
    
print(135-72)