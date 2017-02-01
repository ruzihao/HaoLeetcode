class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        if len(num) > 1:
            sorted_tuples = sorted(enumerate(num), key=lambda x: x[1])
            indices, num = zip(*sorted_tuples)
            q = 0
            p = len(num) - 1
            while q < p:
                if num[q] + num[p] == target:
                    return sorted((indices[q]+1, indices[p]+1))
                elif num[q] + num[p] < target:
                    q += 1
                else:
                    p -= 1
        return None, None

print Solution().twoSum([3,2,4],6)