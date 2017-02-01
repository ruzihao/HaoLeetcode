class Solution:
    # @return an integer
    def romanToInt(self, s):
        # not a string
        if not isinstance(s, str):
            raise ValueError
        # is
        else:
            d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
            # len = 1
            if len(s) == 0:
                return None
            # else
            else:
                # q = 0
                # p = 1
                # res = d[s[q]]
                # trend = 1
                # while q<len(s):
                #     if d[s[q]] > d[s[p]]:
                #         res += d[s[p]]
                #         p += 1
                #     elif d[s[q]] < d[s[p]]:
                #         res -= d[s[p]]
                #         p += 1
                #     else:

                res = 0
                for k in range(len(s)):
                    # if cur >= next
                    if k + 1 < len(s) and d[s[k]] < d[s[k+1]]:
                        # add
                        res -= d[s[k]]
                    # else
                    else:
                        # subtract
                        res += d[s[k]]
                return res

print Solution().romanToInt('MCMXCVI')