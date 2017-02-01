import math

class Solution:
    # @return an integer
    def reverse(self, x):
        # is integer
        if not isinstance(x, int):
            raise ValueError
        else:
            # is nagative
            if x == 0:
                return 0
            elif x < 0:
                # save sign
                is_neg = True
                # get absolute
                x = abs(x)
            else:
                is_neg = False
            # num_digits = int(math.log(x, 10))
            num_digits = int(math.log(x, 10)) + 1
            # do reversing
            # for k in 
            import sys
            rev_x = 0
            for k in range(num_digits, 0, -1):
                # remainder = 
                remainder = x%10
                # quot = 
                x = (x - remainder) / 10
                # rev_x = remainder
                rev_x += remainder * 10**(k-1)
            if is_neg:
                rev_x = -rev_x
            return rev_x

print Solution().reverse(0000000000000000000001)