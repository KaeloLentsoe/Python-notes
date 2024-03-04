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





 