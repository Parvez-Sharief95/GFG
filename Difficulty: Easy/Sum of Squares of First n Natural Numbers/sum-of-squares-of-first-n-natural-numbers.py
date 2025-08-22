#User function Template for python3
import math
class Solution:
    # Function to calculate the sum of squares of first 'number' natural numbers
    def sumOfSquares(self, n):
        # code here
        return sum([pow(i,2) for i in range(1,n+1)])