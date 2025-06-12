class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr) + 1
        st =int( (n * (n+1)) / 2 )
        actual_sum = sum(arr)
        return st - actual_sum