
# Find Maximum

# Write a function named findMinMax that takes an array of numbers as input and returns maximum value.

# " The values should be the maximum numbers in the input array, respectively.

# Sample Input: arr = [15, 2, 34, 8, 19]

# Sample Output: max = maximum(arr) ; // output: max = 34 ;



def findMinMax(arr):
    if not arr:
        return None
    
    maximum = arr[0]
    
    for i in arr:   # Iterating the arr to check the minimum
        if i > maximum:   
            maximum = i  # If the condition matches the value will be equal to min
        
    return maximum  # Returning the value


arr = [15, 2, 34, 8, 19] # arr is defined 
maximum = findMinMax(arr)  # Calling function 

print("max =", maximum)  # Output // max = 34