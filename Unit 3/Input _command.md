#  Input and flow control statement 
## INPUT COMMAND/A BUILT-IN FUNCTION 

In Python, a built-in function is a function that is part of the core Python language and is available for use without the need for importing any external modules. Here are some commonly used built-in functions in Python:

1. **`print()`**: Outputs text or variables to the console.
    ```python
    print("Hello, World!")
    ```

2. **`len()`**: Returns the length of an object, such as a string, list, or tuple.
    ```python
    my_string = "Python"
    print(len(my_string))  # Output: 6
    ```

3. **`input()`**: Reads a line of text from the user's input in the console.
    ```python
    user_input = input("Enter something: ")
    print("You entered:", user_input)
    ```

4. **`type()`**: Returns the type of an object.
    ```python
    my_variable = 42
    print(type(my_variable))  # Output: <class 'int'>
    ```

5. **`int()`**, **`float()`**, **`str()`**: Convert a value to an integer, float, or string, respectively.
    ```python
    num_str = "42"
    num_int = int(num_str)
    print(num_int + 10)  # Output: 52
    ```

6. **`max()`**, **`min()`**: Returns the maximum or minimum value from a sequence.
    ```python
    numbers = [3, 1, 4, 1, 5, 9, 2]
    print(max(numbers))  # Output: 9
    ```

7. **`sum()`**: Returns the sum of elements in a sequence.
    ```python
    numbers = [1, 2, 3, 4, 5]
    print(sum(numbers))  # Output: 15
    ```

8. **`range()`**: Generates a sequence of numbers.
    ```python
    my_range = range(5)
    print(list(my_range))  # Output: [0, 1, 2, 3, 4]
    ```

# More examples 
### Example 1: Basic Input and Output

```python
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to the Python input example.")
```

This program prompts the user to enter their name, and then it prints a personalized welcome message using the entered name.

### Example 2: Numeric Input

```python
age = int(input("Enter your age: "))
next_year = age + 1
print("Next year, you'll be", next_year, "years old.")
```

Here, the `int` function is used to convert the user input to an integer. The program then calculates and prints the user's age for the next year.

### Example 3: Handling Floating-Point Numbers

```python
height = float(input("Enter your height in meters: "))
print("Your height is:", height, "meters.")
```

In this example, the `float` function is used to convert the user input to a floating-point number. The program then prints the entered height.

### Example 4: Multiple Inputs

```python
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("The area of the rectangle is:", area)
```

This program takes the length and width of a rectangle as user inputs, calculates the area, and then prints the result.

### Example 5: Using Input in Conditions

```python
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")
```

Here, the user's age is used in a simple conditional statement to determine if they are eligible to vote.

These examples demonstrate the versatility of the `input` function in Python and how it can be used in various scenarios to interact with the user and handle different types of input.


# "NB"Special one

In Python, the escape sequence **`\n` is used to represent a newline character.** When this character is encountered in a string, it instructs the interpreter to start a new line. Here are a few examples to illustrate the use of `\n` for newline characters:

### Example 1: Basic Newline

```python
print("This is the first line.\nThis is the second line.")
```

Output:
```
This is the first line.
This is the second line.
```

In this example, the `\n` in the string causes a line break between the two sentences.

### Example 2: Multi-line String

```python
multi_line_string = "This is a multi-line string.\nIt spans multiple lines.\nEach line starts with a newline."
print(multi_line_string)
```

Output:
```
This is a multi-line string.
It spans multiple lines.
Each line starts with a newline.
```

Here, the newline characters separate the string into multiple lines, creating a multi-line output.

### Example 3: Input Prompt with Newline

```python
user_name = input("Enter your name:\n")
print("Hello, " + user_name + "!")
```

When the user runs this code, the prompt will appear on a new line, creating a cleaner interface for input.

### Example 4: Formatting Output

```python
age = 25
print("You are {} years old.\nNext year, you'll be {}.".format(age, age + 1))
```

This example uses the `format` method to insert the value of `age` and `age + 1` into the string, with a newline between the sentences.

These examples showcase the use of `\n` for creating newlines in different contexts, whether it's for displaying text in a formatted way, prompting user input, or creating multi-line strings.


# Using Conditional Statements
Conditional statements are necessary for a program to make decisions based upon a set of logical conditions. There are three main constructs in Python for this: ## if, else, and elif Statements

In Python, `if`, `else`, and `elif` statements are used for conditional execution, allowing the program to make decisions based on different conditions. Let's elaborate on each of them and provide a practical example:

### `if` Statement:
The `if` statement is used to check a condition, and if it is true, the indented block of code under the `if` statement is executed.

```python
age = 18

if age >= 18:
    print("You are an adult.")
```

In this example, if the value of `age` is greater than or equal to 18, the message "You are an adult." will be printed.

### `else` Statement:
The `else` statement is used in conjunction with an `if` statement to specify a block of code that should be executed when the `if` condition is false.

```python
age = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

If the value of `age` is less than 18, the message "You are a minor." will be printed.

### `elif` Statement:
The `elif` statement stands for "else if" and is used to check multiple conditions sequentially. It is useful when you have more than two possible outcomes.

```python
score = 75

if score >= 90:
    print("Excellent!")
elif 80 <= score < 90:
    print("Good job!")
elif 70 <= score < 80:
    print("You did okay.")
else:
    print("You need to improve.")
```

In this example, the program evaluates the score and prints different messages based on the score range.

### Practical Example:

Let's combine these statements in a practical example to determine the grading of a student based on their exam score:

```python
exam_score = float(input("Enter your exam score: "))

if 90 <= exam_score <= 100:
    grade = "A"
elif 80 <= exam_score < 90:
    grade = "B"
elif 70 <= exam_score < 80:
    grade = "C"
elif 60 <= exam_score < 70:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)
```

In this example, the program prompts the user for their exam score, evaluates the score, and assigns a corresponding grade. The final grade is then printed.

# Loop and Iterations

Loops are necessary when we need to perform a set of operations several times. The first type of loop we will discuss is called the **while loop.** The while loop checks a logical condition like the if statement. If the condition is true, the code inside the while loop will execute until the condition being checked becomes false. 

And When we execute the code within a loop over and over again, the process is known as **iteration.**

In Python, loops and iterations are used to repeatedly execute a block of code. Two common types of loops are `for` loops and `while` loops. Let's explore both with examples:

### `for` Loop:
The `for` loop is used to iterate over a sequence (such as a list, tuple, string, or range) or other iterable objects.

#### Example 1: Iterating over a List

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

Output:
```
apple
banana
cherry
```

In this example, the `for` loop iterates over each element in the `fruits` list, and the `print` statement prints each fruit.

#### Example 2: Iterating over a Range

```python
for i in range(5):
    print(i)
```

Output:
```
0
1
2
3
4
```

Here, the `for` loop iterates over the range of numbers from 0 to 4, and the `print` statement displays each number.

### `while` Loop:
The `while` loop is used to repeatedly execute a block of code as long as a specified condition is true.

#### Example 1: Countdown

```python
countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1
```

Output:
```
5
4
3
2
1
```

In this example, the `while` loop continues until the `countdown` variable becomes less than or equal to 0. It prints the current value of `countdown` in each iteration.

#### Example 2: User Input Validation

```python
user_input = input("Enter 'quit' to exit: ")

while user_input.lower() != 'quit':
    print("You entered:", user_input)
    user_input = input("Enter 'quit' to exit: ")
```

This program uses a `while` loop to repeatedly prompt the user for input until they enter "quit."

These examples illustrate the basic use of `for` and `while` loops in Python. Loops are powerful constructs that allow you to efficiently repeat code, and they play a crucial role in many programming tasks.

## More examples

Sure, let's delve into a more practical example using a `for` loop to calculate the factorial of a number and a `while` loop to create a simple guessing game.

### Practical Example 1: Calculating Factorial with a `for` Loop

```python
def calculate_factorial(n):
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i

    return factorial

number = int(input("Enter a number to calculate its factorial: "))
result = calculate_factorial(number)
print(f"The factorial of {number} is {result}.")
```

In this example, the program prompts the user to input a number, and then it calculates the factorial of that number using a `for` loop. The `range(1, n + 1)` ensures that the loop iterates from 1 to the given number (inclusive).

### Practical Example 2: Guessing Game with a `while` Loop

```python
import random

secret_number = random.randint(1, 10)
attempts = 0
max_attempts = 3

print("Welcome to the Guessing Game! Try to guess the secret number between 1 and 10.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print(f"Congratulations! You guessed the secret number {secret_number}.")
        break
    else:
        print("Try again!")
        attempts += 1

if attempts == max_attempts:
    print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")
```

In this example, the program generates a random secret number between 1 and 10. The user has up to three attempts to guess the number. The `while` loop continues until the user guesses the correct number or exhausts all attempts.

These practical examples demonstrate how loops can be used for real-world scenarios, such as calculations and interactive games. Loops provide a way to efficiently handle repetitive tasks and create more dynamic and interactive programs.


# Break", "Continue", and "Pass" StatementsPage

In Python, the `break`, `continue`, and `pass` statements are control flow statements that are used within loops and conditional statements to control the flow of the program.

1. **`break` Statement:**
   The `break` statement is used to exit a loop prematurely. When a `break` statement is encountered inside a loop (for loop, while loop, or nested loops), the loop is immediately terminated, and the program continues with the next statement after the loop.

   ```python
   for i in range(5):
       if i == 3:
           break
       print(i)
   ```

   In this example, the loop will print numbers from 0 to 2, and when `i` becomes 3, the `break` statement is executed, and the loop is terminated.

2. **`continue` Statement:**
   The `continue` statement is used to skip the rest of the code inside a loop for the current iteration and move on to the next iteration of the loop.

   ```python
   for i in range(5):
       if i == 2:
           continue
       print(i)
   ```

   In this example, the loop will print numbers from 0 to 4, skipping the iteration where `i` is equal to 2 because of the `continue` statement.

3. **`pass` Statement:**
   The `pass` statement is a no-operation statement. It is used when a statement is syntactically required but no action is desired or needed. It is often used as a placeholder in situations where some code is expected but not yet implemented.

   ```python
   for i in range(3):
       # Some condition that needs handling
       if i == 1:
           pass
       else:
           print(i)
   ```

   In this example, the `pass` statement is used to indicate that no action is taken when `i` is equal to 1. The loop will print 0 and 2.

These statements are particularly useful in controlling the flow of loops and handling specific conditions within the loop body. They provide flexibility in designing loop behavior based on certain conditions and requirements.