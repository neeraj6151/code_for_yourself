"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1
Print the pattern in the function given to you."""
class Solution:
    def pattern11(self, n):
        for i in range(0,n):
            for j in range(0,i+1):
                if((j+1+i) % 2==0):
                    print(0,end=" ")
                else:
                    print(1,end=" ")
            print()