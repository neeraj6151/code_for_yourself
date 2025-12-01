class Solution:    
    def palindromeCheck(self, s):
        rev = s[::-1]
        if s == rev:
            return True
        else:
            return False