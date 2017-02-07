class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        jx = len(nums)-1
        ix = jx
        if len(nums)==1:
            return 1 if nums[jx]!=val else 0
        while ix>=0:
            if nums[jx] == val:
                jx -= 1
                ix -= 1
            else:
                if nums[ix] != val:
                    ix -= 1
                else:
                    nums[ix] = nums[jx]
                    jx -= 1
        return jx+1