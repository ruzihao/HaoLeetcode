class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 != 0:
            return False
        valid_dict = {'(':')', '{':'}', '[':']'}
        valid_set = valid_dict.keys() + valid_dict.values()
        ix, jx = 0, len(s)-1
        while ix<jx:
            if s[ix] not in valid_set or s[jx] not in valid_set:
                return False
            if valid_dict[s[ix]] != s[jx]:
                return False
            ix += 1
            jx -= 1
        return True