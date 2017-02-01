class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        if len(num) < 3:
            return None
        else:
            num.sort()
            left = 0
            min_diff = abs(sum(num[0:3]) - target) + 1
            res = 0
            for left in range(len(num)-2):
                mid = left + 1
                right = len(num) - 1
                while mid < right:
                    s = num[left] + num[mid] + num[right]
                    if s < target:
                        mid += 1
                    elif s > target:
                        right -= 1
                    else:
                        return target
                    if abs(s - target) < min_diff:
                        min_diff = abs(s - target)
                        res = s
            return res

print Solution().threeSumClosest([0, 1, 2], 3)