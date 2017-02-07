class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        lst = []
        s1 = 'qwertyuiop'
        s2 = 'asdfghjkl'
        s3 = 'zxcvbnm'
        for s in words:
            dct = dict.fromkeys(s1+s2+s3, 0)
            sl = s.lower()
            for k in sl:
                dct[k] += 1
            if int(any([dct[k]>0 for k in s1])) + int(any([dct[k]>0 for k in s2])) + int(any([dct[k]>0 for k in s3])) == 1:
                lst.append(s)
        return lst