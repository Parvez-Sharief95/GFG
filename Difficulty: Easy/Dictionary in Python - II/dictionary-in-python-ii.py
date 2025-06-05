# Function to check if pair
# with given sum exists
def pair_sum(dict, arr, sum):
    # code here
    # Hint: You can use 'in' to find if any key is in dict
    if sum == 0:
        return False
    else:
        for i in range(0,len(arr)):
            for j in range(1,len(arr)):
                if arr[i] + arr[j] == sum:
                    return True
    return False
        