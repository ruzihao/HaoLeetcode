class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        s = s.strip()
        len_s = len(s)
        if not len_s:
            return False
        if len_s==1:
            if s[0] in '0123456789':
                return True
            else:
                return False
        else:
            idot = -1
            ie = len_s+1
            ineg = -1
            dotflag = False
            eflag = False
            for i in range(len_s):
                if s[i] in '-0123456789.e':
                    if s[i]=='-' and i!=0:
                        return False
                    if s[i]=='.':
                        if not dotflag:
                            idot = i
                            dotflag = True
                        else:
                            return False
                    if s[i]=='e':
                        if not eflag:
                            ie = i
                            eflag = True
                            if i==0 or i==len_s-1:
                                return False
                        else:
                            return False
                else:
                    return False
            if ie < idot or (idot==0 and ie==1):
                return False
            return True

print Solution().isNumber('.e')
print Solution().isNumber('0')
print Solution().isNumber('.e0')
print Solution().isNumber('0e')
print Solution().isNumber('.4')
print Solution().isNumber('t4')
print Solution().isNumber(' ')
