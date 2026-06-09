
    def reverseString(self, s: str) -> str:
        res = ''
        for i in range(len(s) - 1, -1, -1):
            res = res + s[i]
        return res

#==============================================================================
        res = s[::-1]
        return res