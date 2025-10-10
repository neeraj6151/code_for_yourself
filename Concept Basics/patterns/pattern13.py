"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15
Print the pattern in the function given to you."""
class Solution:
    def pattern13(self, n):
        k=1
        for i in range(0,n):
            for j in range(0,i+1):
                print(k,end=" ")
                k+=1
            print()