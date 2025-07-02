class Solution:
    def findDuplicates(self, arr):
        # code here
        count = {}
        res = []
        
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for key in count:
            if count[key] > 1:
                res.append(key)
        return res
            