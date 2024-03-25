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

## Operator Precedence and Using Parentheses

Operator precedence and the use of parentheses are important concepts in programming and mathematics to determine the order of operations when evaluating expressions. 

### Operator Precedence:

Operator precedence defines the order in which operators are evaluated in an expression. Operators with higher precedence are evaluated before those with lower precedence. For example, in the expression `2 + 3 * 4`, multiplication has a higher precedence than addition, so the multiplication operation is performed first.

Common operator precedence levels (from highest to lowest):

1. Parentheses `( )`
2. Exponentiation `**`
3. Multiplication `*`, Division `/`, Floor division `//`, Modulus `%`
4. Addition `+`, Subtraction `-`
5. Comparison operators `<, >, <=, >=, ==, !=`
6. Logical AND `and`
7. Logical OR `or`
8. Assignment `=`

### Using Parentheses:

Parentheses are used to explicitly specify the order of operations in an expression, overriding the default precedence. Anything enclosed in parentheses is evaluated first. For example:

- `(2 + 3) * 4` ensures that addition is performed first, resulting in `5 * 4`.
- `2 + (3 * 4)` ensures that multiplication is performed first, resulting in `2 + 12`.

Consider the expression `2 + 3 * 4`. Without parentheses, it would be evaluated as `2 + (3 * 4)` due to the higher precedence of multiplication. However, if you want to change the order and perform addition first, you can use parentheses: `(2 + 3) * 4`.

#### Example:

```python
# Without parentheses
result_without_parentheses = 2 + 3 * 4  # Result: 14

# With parentheses
result_with_parentheses = (2 + 3) * 4  # Result: 20
```

In the absence of parentheses, it's essential to be aware of operator precedence to understand how expressions will be evaluated.

In complex expressions, it's often a good practice to use parentheses to make the code more readable and to explicitly convey the intended order of operations.

Understanding operator precedence and using parentheses correctly is crucial for writing correct and predictable code in programming languages.

 ## Relational and Logical Operators

 Relational and logical operators are fundamental components of programming languages, allowing developers to create conditions and make decisions in their code. Let's explore these concepts in more detail:

### Relational Operators:

Relational operators are used to compare two values and determine the relationship between them. These operators return a Boolean value (`True` or `False`) based on the result of the comparison.

1. **Equality (`==`):** Checks if two values are equal.

    ```python
    5 == 5  # True
    "apple" == "orange"  # False
    ```

2. **Inequality (`!=`):** Checks if two values are not equal.

    ```python
    10 != 5  # True
    "cat" != "cat"  # False
    ```

3. **Greater Than (`>`), Less Than (`<`):** Compare if one value is greater than or less than another.

    ```python
    7 > 5  # True
    3 < 2  # False
    ```

4. **Greater Than or Equal To (`>=`), Less Than or Equal To (`<=`):** Check if one value is greater than or equal to, or less than or equal to, another.

    ```python
    10 >= 8  # True
    5 <= 5  # True
    ```

### Logical Operators:

Logical operators allow you to combine or modify conditions, and they operate on Boolean values.

1. **Logical AND (`and`):** Returns `True` if both conditions are true.

    ```python
    (5 > 3) and (10 < 15)  # True
    (3 == 3) and (4 != 5)  # True
    ```

2. **Logical OR (`or`):** Returns `True` if at least one of the conditions is true.

    ```python
    (5 > 10) or (8 < 12)  # True
    (2 == 2) or (7 <= 6)  # True
    ```

3. **Logical NOT (`not`):** Returns the opposite Boolean value.

    ```python
    not (5 > 3)  # False
    not (2 == 2)  # False
    ```

### Combining Relational and Logical Operators:

You can create more complex conditions by combining relational and logical operators. Parentheses are often used to clarify the order of evaluation.

```python
x = 15
y = 8

result = (x > 10) and (y < 5)  # Evaluates to False
```

In the example above, `result` will be `False` because the first condition `(x > 10)` is true, but the second condition `(y < 5)` is false. The `and` operator requires both conditions to be true for the overall result to be true.

Understanding and effectively using relational and logical operators are essential skills for writing conditional statements and controlling the flow of a program. They are commonly used in constructs like `if` statements, loops, and more to make decisions based on certain conditions.

# Operator Precedence Summary:

This is a summary of operator precedence, ordered from the highest to the lowest, encompassing arithmetic, relational, and logical operators.

1. **Parentheses `( )`:**
   - Highest precedence.
   - Anything enclosed in parentheses is evaluated first.

2. **Exponentiation `**`:**
   - Evaluates the power of a number.
   - Example: `2 ** 3` means 2 raised to the power of 3.

3. **Multiplication `*`, Division `/`, Floor division `//`, Modulus `%`:**
   - These arithmetic operators have the same level of precedence.
   - They are evaluated from left to right.
   - Example: `2 * 3 / 4` is equivalent to `(2 * 3) / 4`.

4. **Addition `+`, Subtraction `-`:**
   - These arithmetic operators have the same level of precedence.
   - They are evaluated from left to right.
   - Example: `5 + 2 - 1` is equivalent to `(5 + 2) - 1`.

5. **Relational Operators `<, >, <=, >=, ==, !=`:**
   - Used to compare values.
   - Example: `x > 10` checks if the value of `x` is greater than 10.

6. **Logical NOT `not`:**
   - Unary operator with higher precedence.
   - Example: `not (x > 10)` checks if the value of `x` is not greater than 10.

7. **Logical AND `and`:**
   - Connects two conditions, returning `True` only if both conditions are true.
   - Example: `(x > 5) and (y < 8)` checks if both conditions are true.

8. **Logical OR `or`:**
   - Connects two conditions, returning `True` if at least one condition is true.
   - Example: `(x == 0) or (y == 0)` checks if either condition is true.

9. **Assignment `=`:**
   - Lowest precedence among the operators listed.
   - Used for variable assignment.
   - Example: `result = x + y` assigns the value of `x + y` to the variable `result`.

### Using Parentheses for Explicit Precedence:

While operator precedence rules determine the default order of operations, it's often a good practice to use parentheses to explicitly specify the desired order. This not only makes the code more readable but also avoids any ambiguity.

```python
result = (a + b) * c - (d ** 2)  # Explicit use of parentheses
```

In the expression above, parentheses ensure that addition and subtraction are performed before multiplication and exponentiation, respectively.

Understanding and correctly applying operator precedence is crucial for writing accurate and predictable code in programming languages. Regularly referencing the precedence rules helps avoid errors and ensures the intended order of operations in complex expressions.


