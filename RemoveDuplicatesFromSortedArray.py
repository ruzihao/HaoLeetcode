class Solution:
	# @param a list of integers
	# @return an integer
	def removeDuplicates(self, A):
		q = 0
		p = 1
		while p<len(A):
			if A[q] == A[p]:
				p += 1
			else:
				if q!=p-1:
					A[q+1] = A[p]
				p += 1
				q += 1
		return min(q+1,len(A))

A = [1,1,2]
l = Solution().removeDuplicates(A)
print A[0:l]
