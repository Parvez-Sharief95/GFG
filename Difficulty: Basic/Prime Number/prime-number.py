#User function Template for python3

class Solution:
    def isPrime(self, n):
        # code here
        if n<2:
            return False
        count = 0
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
            
        