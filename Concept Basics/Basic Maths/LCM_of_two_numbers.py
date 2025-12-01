from math import gcd
class Solution:
    def LCM(self, n1, n2):
        return (n1*n2) // gcd(n1,n2)