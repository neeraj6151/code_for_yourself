""" You are given an integer n. Return the value of n! or n factorial.
Factorial of a number is the product of all positive integers less than or equal to that number."""

class Solution:
    def factorial(self, n):
        fact = 1
        if (n == 0):
            return fact
        for i in range(1,n+1):
            fact *= i
        return fact

