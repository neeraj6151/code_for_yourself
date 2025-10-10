"""Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

*****
*****
*****
*****
*****
"""

class Solution:
    def pattern1(self, n):
        for i in range(0,n):
            for j in range(0,n):
                print("*", end="") # By default it will move to next line so need to use end="" to stay on the same line
            print() # No need to put \n in print statement by default empty print() will work over here as it will take \n.
            