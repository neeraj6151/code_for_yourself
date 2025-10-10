"""You are given an integer n. You need to return the number of digits in the number.
The number will have no leading zeroes, except when the number is 0 itself."""

class Solution:
    def countDigit(self, n):
        cnt = 0
        if n==0:
            return 1
        while (n>0):
            cnt+=1
            n = n//10
        return cnt