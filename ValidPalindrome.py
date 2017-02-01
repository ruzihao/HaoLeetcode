class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s != '':
            s = [k for k in s.lower() if k.isalnum()]
            # check palindrome
            for idx  in range(len(s)):
                if s[idx] != s[len(s)-idx-1]:
                    return False
        return True

    def isPalindrome0(self, s):
        if s != '':
            s = s.lower()
            import re
            s = re.sub('[^0-9a-z]*', '', s)

            # check palindrome
            for idx  in range(len(s)):
                if s[idx] != s[len(s)-idx-1]:
                    return False
        return True


print Solution().isPalindrome('')
print Solution().isPalindrome(', ,')
print Solution().isPalindrome('0 aka')
print Solution().isPalindrome('0 ! wp')
