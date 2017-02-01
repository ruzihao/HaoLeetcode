class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        alist = []
        if len(num):
            num = sorted(num)
            # while r
            r = 0
            q = r + 1
            p = len(num) - 1
            while r < len(num):
                if r > 0 and num[r] == num[r-1]:
                    r += 1
                    continue
                q = r + 1
                p = len(num) - 1
                # while q < p
                while q < p:
                    # if sum == 0:
                    sum = num[r] + num[q] + num[p]
                    if sum == 0:
                        # alist append
                        # if (num[r], num[q], num[p]) not in alist:
                        alist.append([num[r], num[q], num[p]])
                        while q < p and num[q] == num[q+1]: q += 1
                        while q < p and num[p] == num[p-1]: p -= 1
                        q, p = q+1, p-1
                    # elif sum < 0:
                    elif sum < 0:
                        # q++
                        q += 1
                    # elif sum > 0:
                    elif sum > 0:
                        # p++
                        p -= 1
                r += 1
        return alist

print Solution().threeSum([-1,0,1,2,-1,-4])