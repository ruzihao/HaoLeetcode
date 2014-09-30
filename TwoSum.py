class Solution:
	def twoSum(self, num, target):
		# do a quicksort
		num_pair = sorted(enumerate(num), key=lambda x: x[1])
		# find the indices
		i1, i2 = 0, len(num_pair)-1
		while i2>i1:
			if num_pair[i1][1]+num_pair[i2][1]==target:
				return tuple(sorted((num_pair[i1][0]+1, num_pair[i2][0]+1)))
			elif num_pair[i1][1]+num_pair[i2][1]<target:
				i1 += 1
			else:
				i2 -= 1
		return (0,0)

if __name__ == '__main__':
	print Solution().twoSum([1,3,4,6,2], 12)
