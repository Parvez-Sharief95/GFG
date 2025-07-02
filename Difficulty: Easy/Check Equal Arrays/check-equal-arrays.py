# User function Template for python3
class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        #code here
        a.sort()
        b.sort()
        
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True