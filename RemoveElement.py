class Solution:
	# @param    A       a list of integers
	# @param    elem    an integer, value need to be removed
	# @return an integer
	def removeElement(self, A, elem):
		q = -1
		p = 0
		while p<len(A):
			if A[p] == elem:
				p += 1
			else:
				if q!=p-1:
					A[q+1] = A[p]
				p += 1
				q += 1
		return min(q+1, len(A))

A = [1,2,3,2]
l = Solution().removeElement(A,2)
print A[0:l]
        

