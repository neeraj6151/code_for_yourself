""" 
Given a string s, representing a large integer, the task is to return the largest-valued odd integer (as a string) that is a substring of the given string s.
The number returned should not have leading zero's. But the given input string may have leading zero. (If no odd number is found, then return empty string.)


Examples:
Input : s = "5347"
Output : "5347"

Explanation :
The odd numbers formed by given strings are --> 5, 3, 53, 347, 5347.
So the largest among all the possible odd numbers for given string is 5347.

Input : s = "0214638"
Output : "21463"

Explanation :
The different odd numbers that can be formed by the given string are --> 1, 3, 21, 63, 463, 1463, 21463.
We cannot include 021463 as the number contains leading zero.
So largest odd number in given string is 21463.

Input : s = "0032579"
Output: "32579"

"""
# Code

class Solution:  
    def largeOddNum(self, s):
        last_index = -1
        first_index = 0
        for c in range(len(s)-1,-1,-1):
            if (int(s[c]) % 2 != 0):
                last_index = c 
                break 
        for i in range(0,len(s)):
            if int(s[i]) != 0:
                first_index = i 
                break 
        if (last_index == -1):
            return ""
        return s[first_index : last_index+1]
