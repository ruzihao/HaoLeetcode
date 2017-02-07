class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return len(nums)
        else:
            ix, jx = 0, 0
            while jx<len(nums):
                if nums[ix] != nums[jx]:
                    nums[ix+1] = nums[jx]
                    ix += 1
                jx += 1
            return ix+1