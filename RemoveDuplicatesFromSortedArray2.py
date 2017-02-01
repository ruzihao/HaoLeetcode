class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        # q -> current position, p -> explore
        if len(A) == 0:
            return 0
        q = 1
        for p in range(1, len(A)):
            # if A[p] == A[q]
            if A[p] != A[p-1]:
                A[q] = A[p]
                q += 1
        return q

print Solution().removeDuplicates([])
print Solution().removeDuplicates([1,1])