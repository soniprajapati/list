# # output=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]

# a=[1, 2, 3, 4, 5, 6]
# i=0
# s=1
# q=0
# b=[]
# p=[]
# while i<len(a):
#     b.append(a[i+q])
#     b.append(a[i])
#     q+=1
#     s+=1
#     j=0
#     while j<len(b):
#         if j==2:
#             p.append(b[i])
#         j+=1
#     i+=1
#     print(p)



nums =  [1,2,3,4,5,6]
list=[]
for i in range(len(nums) - 1):
    result = [nums[i], nums[i + 1]]
    # print(nums)
    list.append(result)
print(list)




