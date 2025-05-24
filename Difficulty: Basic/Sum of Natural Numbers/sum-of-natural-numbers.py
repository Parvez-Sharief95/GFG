
class Solution:
    def seriesSum(self, n : int) -> int:
        # code here
        sum=0
        while(n>0):
            sum = sum+n
            n=n-1
        return sum
        
