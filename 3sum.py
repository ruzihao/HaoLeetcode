class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num) == 0:
            return []

        # sort
        num = sorted(num)

        # initilization
        p = 0
        r = len(num) - 1
        if num[p] + num[r] <0:
            q = r - 1
        else:
            q = p + 1

        # process
        lists = []
        while q>p and q<r:
            import pdb; pdb.set_trace()
            while num[p] + num[q] + num[r] >= 0:
                if q > p+1:
                    q = q - 1
                elif q < r-1:
                    r = r - 1
                else:
                    break
                if num[p] + num[q] + num[r] == 0 and \
                   [num[p], num[q], num[r]] not in lists: 
                    lists.append([num[p], num[q], num[r]])
                # flag = 1
            while num[p] + num[q] + num[r] <= 0:
                if q < r-1:
                    q = q + 1
                elif q > p+1:
                    p = p + 1
                else:
                    break
                if num[p] + num[q] + num[r] == 0 and \
                   [num[p], num[q], num[r]] not in lists: 
                    lists.append([num[p], num[q], num[r]])
            if p == q-1 and r == q+1:
                break
        return lists

print Solution().threeSum([])
print Solution().threeSum([1,2,-2,-1])
print Solution().threeSum([-1,0,1,2,-1,-4])