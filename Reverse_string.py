# Write a function named reverseString that takes a string as input and returns the reverse of the string. 
# Use this function to reverse a given string.

# reversedString = reverseString("hello");

# // Sample Output: reversedString = "olleh"

def reverseString(string):
    reversedString = string[::-1]
    return reversedString

reversedString = reverseString("hello")

print('reversedString = ', reversedString)