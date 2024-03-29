"""
Letter Case Counter Function

Objective:
Write a function named 'case_counter' that counts the number of uppercase and lowercase letters in a given string.

Function Parameter:
text (string): The string in which the letters need to be counted.

Instructions:
- The function should calculate and print two numbers: the count of uppercase letters and the count of lowercase letters in the string.
- If there are no letters of a particular case (uppercase or lowercase) in the string, the function should print 0 for that case.
- Non-alphabetic characters in the string should be ignored and not counted.

Example Test Cases:
1. case_counter("Hello World!") should print the counts of uppercase and lowercase letters.
2. case_counter("PYTHON") should print the counts of uppercase and lowercase letters.
3. case_counter("python") should print the counts of uppercase and lowercase letters.
4. case_counter("1234!@#$") should print 0 for both counts.
"""


def case_counter(text):
    uppercase_count = 0
    lowercase_count = 0

    for char in text:
        if char.isalpha() and char.isupper():
            uppercase_count += 1

        elif char.isalpha () and char.islower():
            lowercase_count += 1

    print(f"Uppercase count: {uppercase_count}, Lowercase count: {lowercase_count}")
    
    # Your code goes here
    # Remember to count uppercase and lowercase letters and ignore non-alphabetic characters
    # Delete this after implementing some code inside this function.


# Test cases
case_counter("Hello World!")
case_counter("PYTHON")
case_counter("python")
case_counter("1234!@#$")
