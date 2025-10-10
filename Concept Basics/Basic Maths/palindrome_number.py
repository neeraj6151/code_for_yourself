"""You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.
A palindrome number is a number which reads the same both left to right and right to left."""

class Solution:
    def isPalindrome(self, n):
        tmp = n
        rev = 0
        while(tmp>0):
            rem = tmp % 10
            rev = rev*10 + rem
            tmp = tmp // 10
        return n==rev


