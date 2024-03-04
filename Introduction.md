# Unit 1: Introduction to Python 3

This unit will introduce you to the Python 3 programming language and cover how to use a platform-independent web-based programming environment to begin writing basic Python scripts. 
We will introduce basic Python data types, the assignment operator, and how to output data to the screen.

 ## History of Python

**Late 1980s: The Birth of Python**
- Python was conceived by Guido van Rossum in the late 1980s.
- Guido van Rossum started working on the implementation of Python at the Centrum Wiskunde & Informatica (CWI) in the Netherlands in December 1989.
- The language's design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than languages like C++ or Java.

**Early 1990s: Python 1.0 and Open Source Release**
- Python 1.0 was released in January 1994. It included many of the features that are still present in the language today.
- Guido van Rossum released Python's source code to the public, making it an open-source project. This decision played a significant role in the language's adoption and community-driven development.

**2000s: Python 2.x and 3.x Transition**
- Python 2.0 was released in 2000, and subsequent versions in the 2.x series were developed and widely used.
- In 2008, Python 3.0 (also known as "Python 3000" and "Py3k") was released with a focus on fixing and enhancing the design of the language. However, due to backward compatibility issues, the adoption of Python 3.x was gradual.

**2010s: Growth, Popularity, and Python 3 Adoption**
- During the 2010s, Python saw tremendous growth in popularity, driven by its versatility, readability, and a vibrant ecosystem of libraries and frameworks.
- The community actively worked on the adoption of Python 3, addressing compatibility issues and encouraging developers to migrate from Python 2 to Python 3.
- The end of official support for Python 2 occurred on January 1, 2020, marking a complete transition to Python 3.

**2020s: Continued Growth and Development**
- Python continues to be one of the most popular programming languages, widely used in various domains, including web development, data science, machine learning, artificial intelligence, automation, and more.
- The Python Software Foundation (PSF) oversees the development of Python and supports the language's community and infrastructure.

Throughout its history, Python has evolved into a powerful and versatile programming language, known for its simplicity, readability, and extensive standard library. The language's community-driven development model and open-source nature have played crucial roles in its success and widespread adoption.

# What is Python? 
- **Flexible programming Language**
- **Design to be human readable**

# Data Types: int and float

Programming languages must distinguish between different types of data. 
There are two numerical data types: int and float found in Python programming language. 

- # **Int**
The `int` data type, short for integer, is used to represent whole numbers without any fractional or decimal parts. Integers can be positive, negative, or zero. Examples of integers include -10, 0, and 357.

Here are some key characteristics and properties of integers:

1. **No Decimal Part:** Integers do not have any digits to the right of the decimal point. They are whole numbers, and any fractional or decimal part is truncated or discarded.

2. **Positive and Negative Values:** Integers can be positive or negative. For example, 10 and -10 are both integers.

3. **Zero is an Integer:** The number zero (0) is also considered an integer. It is neither positive nor negative.

4. **No Size Limitation:** In many programming languages, the `int` data type is designed to handle a wide range of integer values. However, there might be limitations based on the specific programming language and system architecture.

5. **Arithmetic Operations:** Integers support standard arithmetic operations such as addition, subtraction, multiplication, and division. When you perform these operations with integers, the result is always an integer (except for division, where the result may be a floating-point number if the division is not exact).

Example Python code snippet demonstrating the `int` data type:

```python
# Integer examples
integer1 = -10
integer2 = 0
integer3 = 357

# Arithmetic operations
sum_result = integer1 + integer2
product_result = integer2 * integer3
division_result = integer3 / integer1

print("Sum:", sum_result)
print("Product:", product_result)
print("Division:", division_result)
```

In this example, `integer1`, `integer2`, and `integer3` are integers, and the program performs basic arithmetic operations with them. The results, `sum_result`, `product_result`, and `division_result`, will all be integers as well.

- # **Float**
The `float` data type, short for floating-point, is used to represent numbers that can have fractional or decimal parts. Floats are versatile and can represent a wide range of real numbers, including both integers and values with decimal points. Examples of floating-point numbers include 1.3, -3.14, and 300.345567, as you mentioned.

Here are some key characteristics and properties of floating-point numbers:

1. **Decimal Point:** Floating-point numbers have digits to the right of the decimal point, allowing them to represent values that are not whole numbers. The decimal point can appear anywhere in the number.

2. **Positive and Negative Values:** Like integers, floating-point numbers can be both positive and negative. For instance, 1.3 and -3.14 are examples of positive and negative floating-point numbers, respectively.

3. **Scientific Notation:** Floating-point numbers can be expressed in scientific notation, especially when dealing with very large or very small values. For example, 3.0e8 represents 3.0 multiplied by 10 to the power of 8.

4. **Precision Limitations:** Due to the way floating-point numbers are represented in computers, there can be limitations in precision. Some values may not be exactly representable, leading to rounding errors. This can result in issues when comparing floating-point numbers for equality.

5. **Arithmetic Operations:** Floating-point numbers support standard arithmetic operations, including addition, subtraction, multiplication, and division. However, it's important to be aware of precision issues, especially when performing multiple operations.

Example Python code snippet demonstrating the `float` data type:

```python
# Float examples
float1 = 1.3
float2 = -3.14
float3 = 300.345567

# Arithmetic operations
sum_result = float1 + float2
product_result = float2 * float3
division_result = float3 / float1

print("Sum:", sum_result)
print("Product:", product_result)
print("Division:", division_result)
```

In this example, `float1`, `float2`, and `float3` are floating-point numbers, and the program performs basic arithmetic operations with them. The results, `sum_result`, `product_result`, and `division_result`, will all be floating-point numbers.

# Arithmetic Operators

Python supports various arithmetic operators that allow you to perform basic mathematical operations on numbers. Here are the common arithmetic operators in Python:

1. **Addition (`+`):**
   - Example: `a + b`
   - Adds two numbers.

2. **Subtraction (`-`):**
   - Example: `a - b`
   - Subtracts the second number from the first.

3. **Multiplication (`*`):**
   - Example: `a * b`
   - Multiplies two numbers.

4. **Division (`/`):**
   - Example: `a / b`
   - Divides the first number by the second. The result is a float even if the numbers are integers.

5. **Floor Division (`//`):**
   - Example: `a // b`
   - Divides the first number by the second and returns the largest integer less than or equal to the result.

6. **Modulus (`%`):**
   - Example: `a % b`
   - Returns the remainder when the first number is divided by the second.

7. **Exponentiation (`**` or `pow()` function):**
   - Example: `a ** b` or `pow(a, b)`
   - Raises the first number to the power of the second.

Here's a brief example in Python:

```python
a = 10
b = 3

# Addition
result_addition = a + b
print("Addition:", result_addition)

# Subtraction
result_subtraction = a - b
print("Subtraction:", result_subtraction)

# Multiplication
result_multiplication = a * b
print("Multiplication:", result_multiplication)

# Division
result_division = a / b
print("Division:", result_division)

# Floor Division
result_floor_division = a // b
print("Floor Division:", result_floor_division)

# Modulus
result_modulus = a % b
print("Modulus:", result_modulus)

# Exponentiation
result_exponentiation = a ** b
print("Exponentiation:", result_exponentiation)
```

This script demonstrates the use of these operators with the values of `a` and `b`. Remember to handle division carefully, especially if you want integer division or if you are working with floats and want to manage precision.


# Arithmetic Operator Precedence
In Python, arithmetic operators follow a certain precedence order, determining the sequence in which operations are performed when an expression involves multiple operators. Here is the precedence order from highest to lowest:

1. **Parentheses `()`** - Highest precedence
   - Parentheses can be used to explicitly specify the order of operations. Expressions within parentheses are evaluated first.

2. **Exponentiation `**`**
   - Exponentiation has the second-highest precedence. It raises the left operand to the power of the right operand.

3. **Positive `+` and Negative `-` (Unary Operators)**
   - These operators perform unary operations on a single operand. They have higher precedence than most binary operators.

4. **Multiplication `*`, Division `/`, Floor Division `//`, and Modulus `%`**
   - These operators have the same level of precedence and are evaluated from left to right.

5. **Addition `+` and Subtraction `-`**
   - Addition and subtraction have the same level of precedence and are evaluated from left to right.

Here's a quick example demonstrating operator precedence:

```python
result = 2 + 3 * 4 ** 2 - (8 / 2)
print(result)
```

Here's how the expression is evaluated following operator precedence:

1. `4 ** 2` is evaluated first (exponentiation), resulting in 16.
2. `3 * 16` is then evaluated (multiplication), resulting in 48.
3. `8 / 2` is evaluated next (division), resulting in 4.
4. The expression inside the parentheses `(8 / 2)` is subtracted from the result of `3 * 16`.
5. Finally, `2 + (48 - 4)` is calculated, resulting in the final value, which is printed.

Understanding operator precedence is crucial for writing accurate and predictable expressions in Python. If in doubt, you can always use parentheses to explicitly specify the order of operations and improve code readability.

# Syntax and Semantics
Syntax and semantics are fundamental concepts that define the structure and meaning of code.

1. **Syntax:**
   - **Definition:** Syntax refers to the set of rules that dictate the correct combination of symbols and elements in a programming language. It defines the structure and format that a program must follow for the code to be considered valid by the interpreter or compiler.
   - **Example:** In Python, proper syntax includes rules for indentation, correct placement of parentheses, correct use of keywords, proper use of punctuation, and more.
   - **Importance:** Syntax errors occur when code violates the rules of the language, making it impossible for the interpreter or compiler to understand and execute the program. These errors are typically detected during the compilation or interpretation phase.

   ```python
   # Example of correct syntax
   x = 5
   print(x)

   # Example of syntax error
   print("Hello, world!"
   ```

   In the second example, the missing closing parenthesis causes a syntax error.

2. **Semantics:**
   - **Definition:** Semantics, on the other hand, deals with the meaning of the code. It focuses on what a particular combination of symbols (code) does when executed. Semantics are concerned with the logical consequences of the code and how it behaves at runtime.
   - **Example:** If you write a loop, the semantics describe how many times the loop will iterate and what operations will be performed during each iteration. Similarly, if you have a function call, semantics define what that function does and what it returns.
   - **Importance:** Unlike syntax errors, semantic errors do not necessarily prevent the code from running, but they can lead to unexpected or incorrect behavior. Identifying and fixing semantic errors often requires a deeper understanding of the logic and intent behind the code.

   ```python
   # Example of correct semantics
   a = 5
   b = 3
   result = a + b
   print(result)  # Outputs: 8

   # Example of semantic error
   x = "5"
   y = 3
   result = x + y
   print(result)
   ```

   In the second example, a semantic error occurs because the types of `x` and `y` are incompatible for the `+` operation.

Understanding both syntax and semantics is crucial for writing correct and meaningful code. Syntax ensures that the code is well-formed and follows the language rules, while semantics ensure that the code behaves as intended and produces the desired outcomes.


 