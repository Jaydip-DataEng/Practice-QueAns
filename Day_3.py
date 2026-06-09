def sumOfNaturals(n):
    res =0
    if n == 0:
        exit
    else:
        for i in range(n+1):
            res += i
    return res
    
print(sumOfNaturals(0))