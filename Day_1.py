arr = [1,2,3,4,5,6,7,8,9]
output =[]
even =0
odd =0
## one skip one
# for i in arr:
#     if i % 2 == 0:
#         output.append(i)
#     else:
#         continue
#
# print("Output: ",output)
#------------------------------------
## one skip one
# for i in range(len(arr)):
#     if i % 2 ==1:
#         output.append(arr[i])
#     else:
#         continue
#
# print("Output: ",output)
#------------------------------------
## odd even
for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Output: ",odd,even)