class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ix, jx = 0, len(nums)-1
        while ix<jx:
            if nums[ix] == val:
                while nums[jx]==val: 
                    jx -= 1
                nums[ix] = nums[jx]
                jx -= 1
            ix += 1
        return jx+1