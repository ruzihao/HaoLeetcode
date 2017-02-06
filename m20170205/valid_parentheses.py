class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 != 0:
            return False
        valid_dict = {')':'(', '}':'{', ']':'['}
        count_dict = dict.fromkeys(valid_dict.values(), 0)
        valid_set = valid_dict.keys() + valid_dict.values()
        for ix in range(len(s)):
            if s[ix] not in valid_set:
                return False
            if s[ix] in valid_dict.values():
                count_dict[s[ix]] += 1
            else:
                count_dict[valid_dict[s[ix]]] -= 1
            if any([k<0 for k in count_dict.values()]):
                return False
        if any([k!=0 for k in count_dict.values()]):
            return False
        return True