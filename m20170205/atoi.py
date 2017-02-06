class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not len(str):
            return 0
        pos = True
        if str[0]=='+':
            pos = True
            str = str[1:]
        elif str[0]=='-':
            pos = False
            str = str[1:]
        else:
            str_len = len(str)
            res = 0
            for ix, k in enumerate(str):
                if not (k.isdigit() or k=='.'):
                    return 0
                elif k=='.':
                    return res if pos else -res
                else:
                    res += int(k) * 10**(str_len-ix-1)
        return res if pos else -res
                