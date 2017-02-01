class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not len(strs):
            return ''
        else:
            com = strs[0]
            for k in range(1, len(strs)):
                p = 0
                while p < min(len(com), len(strs[k])) and com[p] == strs[k][p]:
                    p += 1
                com = com[0:p]
            return com

print Solution().longestCommonPrefix(['ab', 'abs'])