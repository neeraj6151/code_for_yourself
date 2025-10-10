""" You are given an integer n. Return the largest digit present in the number."""

class Solution:
    def largestDigit(self, n):
        large = 0
        while(n>0):
            digit = n % 10
            if(digit>large):
                large = digit
            n  = n // 10
        return large