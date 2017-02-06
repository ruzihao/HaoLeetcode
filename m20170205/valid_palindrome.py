class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid_set = 'abcdefghijklmnopqrstuvwxyz' + '0123456789'
        ix, jx = 0, len(s)-1
        while ix<=jx:
            if s[ix] != s[jx]:
                return False
            if s[ix] not in valid_set:
                ix += 1
                continue
            if s[jx] not in valid_set:
                jx -= 1
                continue
        return True