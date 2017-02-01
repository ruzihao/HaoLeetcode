# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        def cal_slope(p1, p2):
            if p1.y == p2.y:
                return 0
            elif p1.x == p2.x:
                return 
        if not len(points):
            # if empty, return
            return None
        else:
            for i in range(points):
                # take one point
                for j in range(points):
                    if j != i:

                # calculate the slope with every other point
                # find the slope of the line on which there are most number of points
        # return the slope