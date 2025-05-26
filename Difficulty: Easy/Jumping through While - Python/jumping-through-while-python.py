# Function to print x in increasing order
def printIncreasingPower(x):
    ##Your code here
    i=1
    res=i**2
    # Loop to jump in powers of 2
    while(x>=res):
        ##Your code here
        print (res , end = " ")
        ##Your code here
        i+=1
        res=i**2
    