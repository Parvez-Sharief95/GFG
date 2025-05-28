#User function Template for python3

arr = tuple(map(int, input().split()))
x = int(input())

########### Write your code below ###############
# Print the index of x in arr
for i in range(0,len(arr)+1):
    if x == arr[i]:
        print(i)
########### Write your code above ###############