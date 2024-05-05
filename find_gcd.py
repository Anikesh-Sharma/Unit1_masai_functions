# Write a function named findGCD that takes two integers as input and returns their greatest common divisor (GCD). Use this function to find the GCD of two given numbers.

# gcdResult = findGCD(36, 48);

# // Sample Output: gcdResult = 12

def findGCD(a, b):
    while b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# Example usage:
num1 = 36
num2 = 24
gcf = findGCD(num1, num2)
print('gcdResult = ',gcf)  
