class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle)==0:
            return 0
        if len(haystack)<len(needle):
            return -1
        else:
            for ix in range(len(haystack)-len(needle)+1):
                if haystack[ix:ix+len(needle)]==needle:
                    return ix
            return -1