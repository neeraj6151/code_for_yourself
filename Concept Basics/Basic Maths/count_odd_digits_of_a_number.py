"""You are given an integer n. You need to return the number of odd digits present in the number.
The number will have no leading zeroes, except when the number is 0 itself."""

class Solution:
    def countOddDigit(self, n):
        odd_cnt = 0
        while(n>0):
            if(n%2!=0):
               odd_cnt += 1
            n = n//10
        return odd_cnt