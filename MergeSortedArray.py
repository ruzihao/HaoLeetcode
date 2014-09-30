class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        p = m-1
        q = n-1
        r = m+n-1
        while p>=0 and q>=0:
            if A[p]>=B[q]:
                A[r] = A[p]
                p -= 1
                r -= 1
            else:
                A[r] = B[q]
                q -= 1
                r -= 1
        if r>=0 and p<0:
            A[0:r+1] = B[0:r+1]
        return

B = [4,5,6]
A = [1,2,3] + [0]*len(B)
Solution().merge(A, len(A)-len(B), B, len(B))
print A

