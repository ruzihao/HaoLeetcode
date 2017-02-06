class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0 or len(s)%2 != 0:
            return False
        valid_dict = {')':'(', '}':'{', ']':'['}
        stack = [''] * len(s)
        valid_set = valid_dict.keys() + valid_dict.values()
        ix, jx = 0, 0
        while ix<len(s):
            if s[ix] not in valid_set or s[jx] not in valid_set:
                return False
            if s[ix] in valid_dict.values():
                stack[jx] = s[ix]
                jx += 1
            else:
                if jx==0 or stack[jx-1]!=valid_dict[s[ix]]:
                    return False
                else:
                    jx -= 1
            ix += 1
        if jx>0:
            return False
        return True