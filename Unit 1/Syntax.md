# Note about syntax

In Python, reserved words, also known as keywords, are predefined and have specific meanings within the language. These words cannot be used as variable names or identifiers because they are reserved for specific purposes. Attempting to use a keyword as a variable name will result in a syntax error.

here's a brief overview of some of the commonly used Python keywords:

1. **Logical Operations:**
   - `and`: Logical AND operator
   - `or`: Logical OR operator
   - `not`: Logical NOT operator

2. **Control Flow:**
   - `if`: Used for conditional statements
   - `else`: Used in conjunction with `if` for an alternative branch
   - `elif`: Stands for "else if" and is used for multiple branches in conditional statements
   - `while`: Used for creating loops with a specified condition
   - `for`: Used for iterating over a sequence (e.g., a list or string)
   - `break`: Used to exit a loop prematurely
   - `continue`: Skips the rest of the loop's code and continues with the next iteration

3. **Function and Class Definitions:**
   - `def`: Used to define a function
   - `class`: Used to define a class

4. **Exception Handling:**
   - `try`: Starts a block of code that might throw an exception
   - `except`: Specifies a block of code to be executed if an exception occurs
   - `finally`: Specifies a block of code to be executed, regardless of whether an exception occurred or not
   - `raise`: Raises an exception

5. **Importing Modules:**
   - `import`: Used to import modules into your code
   - `from`: Allows importing specific attributes or functions from a module

6. **Miscellaneous:**
   - `True`, `False`: Boolean literals
   - `None`: Represents the absence of a value or a null value
   - `as`: Used for creating an alias when importing modules or renaming variables

*To get an up-to-date and comprehensive list of Python keywords, you can refer to the official Python Language Reference documentation. As mentioned in your question, section 2.3.1 of the Python Language Reference provides the list of keywords specific to the version you are using. It's always a good practice to check the official documentation for the most accurate and current information.*

# Syntax and Semantic Errors
The provided content discusses two categories of errors in Python: syntax errors and semantic errors.

1. **Syntax Errors:**
   - **Definition:** Syntax errors occur when you write expressions or statements that do not follow Python's syntax rules.
   - **Example:** The content provides an example of a syntax error: `13 = age`. This is incorrect because an assignment statement must have a variable on the left-hand side (LHS) of the assignment operator "=".
   - **Explanation:** Python checks the syntax of your code during the parsing phase and raises a syntax error if it encounters statements or expressions that do not conform to the language's syntax rules.

2. **Semantic Errors:**
   - **Definition:** Semantic errors occur when the Python interpreter cannot evaluate expressions or execute statements because they lack a meaningful association or context.
   - **Example:** The content provides an example of a semantic error: `age + 1`. This expression is well-formed but has meaning only when `age` is already assigned a value. If evaluated before assigning a value to `age`, Python raises a semantic error.
   - **Explanation:** Semantic errors are not caught during the parsing phase but rather during runtime. They indicate logical mistakes in the program, such as trying to perform operations on variables before they are properly initialized.
