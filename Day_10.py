def utility(s):
    out = ''
    for i in range(0, len(s) - 1):
        if i % 2 == 0:
            out = out + s[i]
        else:
            continue
    return out

print(utility('EBAHXuIocNhypBVEeKNaKPtBvIjHpRkAkCwcaZgqkIIvqlRJelSCmQyFljHAawYNgyxnwVYuGOlgXRIayYJFyMvPjdLaWuzwdDRh'))