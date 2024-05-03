# Write a function named findMinMax that takes an array of numbers as input and returns the minimum value present in the array. The values should be the minimum numbers in the input array, respectively.

# Sample Input: arr = [15, 2, 34, 8, 19]

# Sample Output: min = minimum(arr) ;

# //output: min = 2 ;


def findMinMax(arr):
    if not arr:
        return None
    
    minimum = arr[0]
    
    for i in arr:   # Iterating the arr to check the minimum
        if i < minimum:   
            minimum = i  # If the condition matches the value will be equal to min
        
    return minimum  # Returning the value


arr = [15, 2, 34, 8, 19] # arr is defined 
minimum = findMinMax(arr)  # Calling function 

print("min =", minimum)  # Output // min = 2