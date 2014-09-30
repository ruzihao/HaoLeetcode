class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
		if not s:
			return 0
		else:
			s = s.strip()
			n = len(s)-1
			n0 = n
			while n0>=0:
				if s[n0]==' ':
					break
				n0 -= 1
			return n-n0


print Solution().lengthOfLastWord('a ')
