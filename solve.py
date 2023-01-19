import math
lis = [1,2,3,4,5,0]
maxi = max(lis)
ans = 0
for i in lis:
    if i>ans and ans<maxi:
        ans = i

print(ans)

print(sorted(lis))