# String 2.0 

## **Going Deeper with Strings**

### A string is sequence 
A string is a sequence of characters. 
- You can access the characters one at a time with the bracket operator. 

# String Methods
There are a host of methods available for processing string objects. 

## String objects 
a string is a sequence of characters enclosed within single quotes (`'`) or double quotes (`"`). Strings are immutable, meaning once they are created, their contents cannot be changed.

Here are some key points about string objects in Python:

1. **Creation**: Strings can be created by enclosing characters within single quotes or double quotes.

    ```python
    string1 = 'Hello, World!'
    string2 = "Python Programming"
    ```

2. **Immutable**: Once a string object is created, its contents cannot be changed. You cannot modify individual characters in a string directly.

    ```python
    string = "Python"
    string[0] = 'C'  # This will raise an error
    ```

3. **Accessing Characters**: Characters in a string can be accessed using indexing. Indexing starts from 0 for the first character, -1 for the last character, -2 for the second last character, and so on.

    ```python
    string = "Python"
    print(string[0])    # Output: P
    print(string[-1])   # Output: n
    ```

4. **Slicing**: You can extract substrings from a string using slicing, which allows you to specify a range of indices.

    ```python
    string = "Python"
    print(string[2:5])  # Output: tho
    ```

5. **Concatenation**: Strings can be concatenated using the `+` operator.

    ```python
    string1 = "Hello"
    string2 = "World"
    concatenated_string = string1 + ", " + string2
    print(concatenated_string)  # Output: Hello, World
    ```

6. **String Methods**: Python provides numerous built-in methods for working with strings, such as `split()`, `join()`, `upper()`, `lower()`, `strip()`, `replace()`, and many more.

    ```python
    string = "  Python Programming  "
    print(string.strip())      # Output: Python Programming
    print(string.upper())      # Output:   PYTHON PROGRAMMING  
    print(string.replace('o', '0'))  # Output:   Pyth0n Pr0gramming  
    ```

7. **Formatted Strings**: Python allows you to create formatted strings using f-strings or the `format()` method.

    ```python
    name = "Alice"
    age = 30
    print(f"My name is {name} and I am {age} years old.")
    ```

8. **String Operations**: You can perform various operations on strings, such as checking for substring existence, finding the length of a string, and more.

    ```python
    string = "Python Programming"
    print(len(string))          # Output: 18
    print('Pro' in string)      # Output: True
    print(string.index('Pro'))  # Output: 7
    ```

*Strings are fundamental data types in Python, and they are extensively used in various programming tasks, such as text processing, data manipulation, and more. Understanding string objects and their operations is essential for effective Python programming.*


