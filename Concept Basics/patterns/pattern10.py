"""Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

*
**
***
****
*****
****
***
**
*
Print the pattern in the function given to you."""

class Solution:
    def pattern10(self, n):
        self.first_part(n)
        self.second_part(n-1)
    def first_part(self,n):
        for i in range(0,n):
            for j in range(0,i+1):
                print("*",end="")
            print()
    def second_part(self,n):
        for i in range(0,n):
            for j in range(0,n-i):
                print("*",end="")   
            print()

if __name__  == "__main__":
    N = int()
    sol = Solution()
    sol.pattern10(N)
        