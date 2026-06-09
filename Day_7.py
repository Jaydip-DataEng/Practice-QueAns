arr= [1,2,3,4,5,6,7,8,9]

print(len(arr))


def swapKth(self, arr, k):
    # Code Here
    res = arr
    res[k - 1], res[len(arr) - (k)] = res[len(arr) - (k)], res[k - 1]
    return res
#===============================================================================
def isPrime(self, n):
        start =2
        end =n//2
        if n == 1:
            return False
        for x in range(start,end):
            if n%x==0:
                return False
        return True