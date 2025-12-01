from math import sqrt 
class Solution:
    def __init__(self):
        self.cnt = 0

    def isPrime(self, n):
        if n < 2:
            return False
        for i in range(2,int(sqrt(n))+1):
            if (n%i == 0):
                return False
        return True

    def primeUptoN(self, n):
        for i in range(2,n+1):
            if (self.isPrime(i)):
                self.cnt += 1
        return self.cnt