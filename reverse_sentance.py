# Write a function named reverseSentence that takes a sentence (a string containing words separated by spaces) as input and returns the sentence with its words reversed.

# Sample Input: "Hello World" Sample Output: "olleH dlroW"


def reverse_sentence(string):
    words = string.split() 
    reversed_words = [char[::-1] for char in words] 
    reverse_string = ' '.join(reversed_words)
    return reverse_string

string = 'Hello World'
reverse_string = reverse_sentence(string)
print(reverse_string) 
