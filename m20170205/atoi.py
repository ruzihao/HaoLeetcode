class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        max_int = 2147483647
        min_int = -2147483648
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
            if pos and ((res==max_int/10 and int(k)>7) or res>max_int/10):
                return max_int
            if not pos and ((res==max_int/10 and int(k)>8) or res>max_int/10):
                return min_int
            res = res*10 + int(k)
        return res if pos else -res