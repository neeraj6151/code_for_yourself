import math

class Solution:

    """ Function to count the 
    number of digits in N """
    def countDigit(self, n):
        
        # Base case
        if n == 0:
            return 1

        count = int(math.log10(n)) + 1
        return count
    
    """ Function to find whether the
    number is Armstrong or not """
    def isArmstrong(self, n):
        # Store the count of digits
        count = self.countDigit(n)
        
        # Variable to store the sum
        sum = 0
        
        # Variable to store the copy
        copy = n
        
        # Iterate through each
        # digit of the number
        while n > 0:
            
            # Extract the last digit
            lastDigit = n % 10
            
            # Update sum
            sum += pow(lastDigit, count)
            
            # Remove the last digit
            # from the number
            n = n // 10
        
        # Check if the sum of digits raised to the
        # power of k equals the original number
        if sum == copy:
            return True
        return False
        
# Main function
if __name__ == "__main__":
    n = int()
    sol = Solution()
    res = str(sol.isArmstrong(n))
    res = res.replace(" ", "")
    print(res)