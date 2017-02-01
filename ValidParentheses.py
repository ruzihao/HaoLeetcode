''' Accepted 30Sept2014 '''
class Solution:
    # @return a boolean
    def isValid(self, s):
        match = lambda x, y: (x=='(' and y==')') or (x=='[' and y==']') or (x=='{' and y=='}')
        sta = []
        for k in s:
            if len(sta) == 0:
                sta.append(k)
                continue
            if match(sta[-1], k):
                sta.pop()
            else:
                sta.append(k)

        if len(sta) != 0:
            return False
        return True

print Solution().isValid('([)]')