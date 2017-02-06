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
            
        str_len = len(str)
        res = 0
        for ix, k in enumerate(str):
            if not k.isdigit():
                break
            res = res*10 + int(k)
        return res if pos else -res
                