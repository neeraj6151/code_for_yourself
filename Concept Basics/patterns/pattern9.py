"""Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
    * 
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
Print the pattern in the function given to you."""

class Solution:
    def pattern9(self, n):
        self.first_part(n)
        self.second_part(n)

    # Print upper part for the pattern
    def first_part(self,n):
        for i in range(0,n):
            for j in range(0,n-i-1):
                print(" ",end="")
            for j in range(0,2*i+1):
                print("*",end="")
            for j in range(0,n-i-1):
                print(" ",end="")
            print()

    # Print lower part for the pattern
    def second_part(self,n):
        for i in range(0,n):
            for j in range(0,i):
                print(" ",end="")
            for j in range(0,(2*n-1)-(2*i)):
                print("*",end="")
            for j in range(0,i):
                print(" ",end="")
            print()

if __name__ == "__main__":
    N = int()

    sol = Solution()

    sol.pattern9(N)

