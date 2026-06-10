import copy
def isPalindrome( arr):
    # code here
    i = 0
    j = len(arr) - 1
    arr1 = copy.deepcopy(arr)
    while (i < j):
        arr1[i], arr1[j] = arr1[j], arr1[i]
        i += 1
        j -= 1

    if arr1 == arr:
        return True
    else:
        return False

print(isPalindrome([1,10,10,7,7]))

#================================
# arr1 = arr[::-1]
# if arr == arr1:
#     return True
# else:
#     return False
