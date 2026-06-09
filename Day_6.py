# def isIsogram(s):
#     res = {}
#     for char in s:
#         if char in res:
#             return False
#         else:
#             res[char] = 1
#     return True

#=====================================================================

# def isIsogram(self, s):
#     val = []
#     val2 = []
#     for i in range(len(s)):
#         val = s[i]
#         for j in range(i + 1, len(s)):
#             val2 = s[j]
#             if val == val2:
#                 return False
#
#     return True
#========================================================================
def delAlternate (s):
    res =""
    for i in range(len(s)):
        if i%2==0 :
            res = res + s[i]
            continue
    return res

print(delAlternate('Geeks'))