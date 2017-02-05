class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            x = 1/x if x!=0 else 0
        elif n==0:
            return 1
        else:
            y = 1
            for k in range(n):
                y *= x
        return y