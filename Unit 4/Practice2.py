# Creation
string_1 = 'Hello, World!'
string_2 = "Python Programming"

# Accessing Characters
print(string_1[0])    # Output: H
print(string_2[-1])   # Output: g

# Slicing
print(string1[2:5])  # Output: llo
print(string2[:6])   # Output: Python

# Concatenation
concatenated_string = string1 + " " + string2
print(concatenated_string)  # Output: Hello, World! Python Programming

# String Methods
string = "  Python Programming  "
print(string.strip())              # Output: Python Programming
print(string.upper())              # Output:   PYTHON PROGRAMMING  
print(string.replace('o', '0'))    # Output:   Pyth0n Pr0gramming  

# Formatted Strings
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alice and I am 30 years old.

# String Operations
string = "Python Programming"
print(len(string))          # Output: 18
print('Pro' in string)      # Output: True
print(string.index('Pro'))  # Output: 7
