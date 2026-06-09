def convertFive(n):
    new = str(n)
    res = ""
    # for i in range(len(new)):
    #     if new[i] == '0':
    #         res = res + '5'
    #     else:
    #         res += new[i]
    #         continue
    # return res
##-----------------------------------------------------
#     for char in new:
#         if char == '0':
#             res = res + '5'
#         else:
#             res += char
#     return res
#
# print(convertFive(10013402104))

## -----------------------------------------------------
def modify(s):
    new = ''
    for i in s:
        if s[0].isupper():
            new = s.upper()
        else:
            new = s.lower()

    return new

print(modify("avDC"))