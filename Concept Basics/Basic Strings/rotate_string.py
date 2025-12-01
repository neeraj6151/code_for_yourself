"""
Problem => Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.


Examples:
Input : s = "abcde" , goal = "cdeab"
Output : true

Explanation : After performing 2 shifts we can achieve the goal string from string s.
After first shift the string s is => bcdea
After second shift the string s is => cdeab.

Input : s = "abcde" , goal = "adeac"
Output : false

Explanation : Any number of shift operations cannot convert string s to string goal.

Input : s = "abcde" , goal = "abcde"
Output: true

"""

# code

class Solution:    
    def rotateString(self, s, goal):
        left = ""
        for i in range(len(s)):
            right = s[i:]
            res = right + left
            left += s[i]
            if(res == goal):
                return True
        return False
