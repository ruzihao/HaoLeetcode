class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carr = 1
        for ix in range(len(digits))[::-1]:
            if digits[ix] != 9 and carr:
                digits[ix] += carr
                carr = 0
                break
            else:
                digits[ix] = 0
        if carr:
            return [1] + digits
        else:
            return digits