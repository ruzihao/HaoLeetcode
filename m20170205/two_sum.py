class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for ix in range(len(nums)):
            for jx in range(ix+1, len(nums)):
                if nums[ix] + nums[jx] == target:
                    return [ix, jx]