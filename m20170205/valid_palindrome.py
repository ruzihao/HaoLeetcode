class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid_set = 'abcdefghijklmnopqrstuvwxyz' + '0123456789'
        s = s.lower()
        ix, jx = 0, len(s)-1
        while ix<=jx:
            if s[ix] not in valid_set:
                ix += 1
                continue
            if s[jx] not in valid_set:
                jx -= 1
                continue
            if s[ix] != s[jx]:
                return False
            ix += 1
            jx -= 1
        return True