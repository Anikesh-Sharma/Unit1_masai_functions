# Write a function named calculateFactorial that takes an integer n as input and returns the factorial of n (n!). Use this function to calculate the factorial of a given number.

# result = calculateFactorial(5);

# // Sample Output: result = 120

def calculateFactorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact
    
fact = calculateFactorial(5)
print(fact)

