class Solution:
	# @return an integer
	# Just need to go over the sequence once
	def lengthOfLongestSubstring(self, s):
		p1 = 0
		p2 = p1
		max_len = 0
		sub = {}
		while p1<len(s) and p2<len(s):
			if not sub.get(s[p2],False):
				sub[s[p2]] = True
				max_len = max(max_len, p2-p1+1)
				p2 += 1
			else:
				max_len = max(max_len, p2-p1)
				sub[s[p1]] = False
				p1 += 1
		return max_len

def main():
	print Solution().lengthOfLongestSubstring('wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco')
	print Solution().lengthOfLongestSubstring('qopubjguxhxdipfzwswybgfylqvjzhar')

if __name__ == '__main__':
	main()

