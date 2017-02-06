class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_sorted = sorted(nums)
        lst = []
        for ix in range(len(nums_sorted)):
            if ix>0 and nums_sorted[ix]==nums_sorted[ix-1]:
                continue
            lst.extend(self.twoSum(nums_sorted[ix], nums_sorted[ix+1:]))
        return lst
            
    def twoSum(self, s, nums):
        lst = []
        ix = 0
        jx = len(nums)-1
        while(True):
            if ix>0 and nums[ix]==nums[ix-1]:
                continue
            if jx<=ix:
                break
            if nums[ix] + nums[jx] > -s:
                jx -= 1
            elif nums[ix] + nums[jx] < -s:
                ix += 1
            else:
                lst.append([s, nums[ix], nums[jx]])
                ix += 1
        return lst


if __name__ == '__main__':
    sl = Solution()
    print sl.threeSum([3,0,-1,1,2])