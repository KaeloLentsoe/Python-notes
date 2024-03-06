# Operators
## Practice With Arithmetic Operators

Python supports a variety of operators that allow you to perform operations on variables and values. Here are some of the common types of operators in Python:

1. **Arithmetic Operators:**
   - `+` (Addition)
   - `-` (Subtraction)
   - `*` (Multiplication)
   - `/` (Division)
   - `%` (Modulus - remainder of the division)
   - `**` (Exponentiation)
   - `//` (Floor division - division rounded down to the nearest whole number)

   Example:
   ```python
   a = 5
   b = 2

   addition = a + b  # 7
   subtraction = a - b  # 3
   multiplication = a * b  # 10
   division = a / b  # 2.5
   modulus = a % b  # 1
   exponentiation = a ** b  # 25
   floor_division = a // b  # 2
   ```

2. **Comparison Operators:**
   - `==` (Equal to)
   - `!=` (Not equal to)
   - `<` (Less than)
   - `>` (Greater than)
   - `<=` (Less than or equal to)
   - `>=` (Greater than or equal to)

   Example:
   ```python
   x = 5
   y = 10

   equal = x == y  # False
   not_equal = x != y  # True
   less_than = x < y  # True
   greater_than = x > y  # False
   less_than_equal = x <= y  # True
   greater_than_equal = x >= y  # False
   ```

3. **Logical Operators:**
   - `and` (Logical AND)
   - `or` (Logical OR)
   - `not` (Logical NOT)

   Example:
   ```python
   p = True
   q = False

   logical_and = p and q  # False
   logical_or = p or q  # True
   logical_not = not p  # False
   ```

4. **Assignment Operators:**
   - `=` (Assignment)
   - `+=` (Addition assignment)
   - `-=` (Subtraction assignment)
   - `*=` (Multiplication assignment)
   - `/=` (Division assignment)
   - `%=` (Modulus assignment)
   - `**=` (Exponentiation assignment)
   - `//=` (Floor division assignment)

   Example:
   ```python
   x = 5
   x += 3  # Equivalent to x = x + 3 (x is now 8)
   ```

5. **Identity Operators:**
   - `is` (True if the operands are identical)
   - `is not` (True if the operands are not identical)

   Example:
   ```python
   a = [1, 2, 3]
   b = a
   c = [1, 2, 3]

   print(a is b)  # True
   print(a is c)  # False
   print(a is not c)  # True
   ```

6. **Membership Operators:**
   - `in` (True if a value is found in the sequence)
   - `not in` (True if a value is not found in the sequence)

   Example:
   ```python
   my_list = [1, 2, 3, 4]

   print(2 in my_list)  # True
   print(5 not in my_list)  # True
   ```

These are some of the basic operators in Python. Understanding how to use them is essential for writing effective and expressive code.