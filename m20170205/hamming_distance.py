class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        dis = 0
        if x>y:
            x, y = y, x
        while y>0:
            xr, yr = x%2, y%2
            x = (x - xr)/2
            y = (y - yr)/2
            if xr!=yr:
                dis += 1
        return dis