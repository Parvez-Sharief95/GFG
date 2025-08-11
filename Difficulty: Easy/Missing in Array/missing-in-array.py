class Solution:
    def missingNum(self, arr):
        # code here
        n= len(arr)
        sumof =0
        tsum =0
        for i in range(n):
            sumof = sumof + arr[i]
        for i in range(1,n+2):
            tsum = tsum + i
        return tsum - sumof