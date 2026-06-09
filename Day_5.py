# ans = float('-inf')
# for number in arr:
#     if number > ans:
#         ans = number
#     else:
#         continue
# return ans
#===========================================================

# ans = float('-inf')
# for i in range(len(arr)):
#     if arr[i] > ans:
#         ans = arr[i]
#     else:
#         continue
# return ans

#===================================================================

def search(arr, x):
    # code here
    ans = 0
    for i in range(len(arr)):
        if arr[i] == x:
            ans = i
            break
        else:
            ans = -1
    return ans
print(search([5,23,3,1,4,1,2],1))