class Solution:
    # @return an integer
    def atoi(self, s):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        s = s.strip(' ')
        k = 0
        pos = True
        if len(s) and s[0] in '0123456789-+':
            pos = False if s[0] == '-' else True 
            s = s[1:] if s[0] in '+-' else s
            for i in xrange(0, len(s)):
                if not s[i] in '0123456789': # whether a letter
                    return k if pos else -k
                elif k > int(INT_MAX/10) or (k == int(INT_MAX/10) and int(s[i])>8-int(pos)): # whether over the limit
                    return INT_MAX if pos else INT_MIN
                else:
                    k = k*10 + int(s[i])
        return k if pos else -k

print Solution().atoi("-0012a42")
