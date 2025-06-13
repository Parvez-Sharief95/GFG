#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	n = len(arr)
    	pos = 0
    	for i in range(len(arr)):
    	    if arr[i] != 0:
    	        arr[pos] = arr[i]
    	        pos +=1
    	        
    	while pos < n:
    	     arr[pos] = 0
    	     pos +=1
    	return arr