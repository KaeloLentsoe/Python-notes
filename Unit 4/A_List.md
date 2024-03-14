# Indexing

Indexing in Python typically refers to accessing individual elements within a data structure like *lists, tuples, strings, or dictionaries.* Each element in such data structures is assigned a unique index, starting from 0 for the first element, 1 for the second, and so on.

### A brief overview of indexing in Python:

1. **Indexing Lists**: Lists are ordered collections of items, and you can access individual elements using square brackets `[]` along with the index of the element you want to access.

    ```python
    my_list = [1, 2, 3, 4, 5]
    print(my_list[0])  # Output: 1
    print(my_list[2])  # Output: 3
    ```

2. **Indexing Strings**: Strings in Python are also sequence-like objects, so you can access individual characters using indexing.

    ```python
    my_string = "Hello, World!"
    print(my_string[0])  # Output: 'H'
    print(my_string[7])  # Output: 'W'
    ```

3. **Negative Indexing**: Python allows negative indexing where `-1` refers to the last element, `-2` refers to the second last, and so on.

    ```python
    my_list = [1, 2, 3, 4, 5]
    print(my_list[-1])  # Output: 5
    print(my_list[-2])  # Output: 4
    ```

4. **Slicing**: In addition to single element indexing, Python also supports slicing to extract a portion of the sequence. The syntax is `start:stop:step`.

    ```python
    my_list = [1, 2, 3, 4, 5]
    print(my_list[1:4])  # Output: [2, 3, 4]
    ```

5. **Dictionary Indexing**: Dictionaries use keys for indexing rather than numerical indices. You can access values using keys.

    ```python
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(my_dict['a'])  # Output: 1
    ```

Indexing allows for efficient access to elements within data structures, enabling manipulation and processing of data in Python programs.


# Lists - A list is a sequence

Lists are one of the most versatile and commonly used data structures. They are used to store collections of items, and each item in a list is called an *element*. 
- Lists can contain elements of different types, making them flexible for various programming tasks. 

Here's a brief overview of list operations and features in Python:

1. **Creating Lists**: You can create a list by enclosing comma-separated values within square brackets `[]`.

    ```python
    my_list = [1, 2, 3, 4, 5]
    ```

2. **Accessing Elements**: You can access individual elements of a list using indexing, similar to strings.

    ```python
    print(my_list[0])  # Output: 1
    print(my_list[-1])  # Output: 5
    ```

3. **Slicing Lists**: Slicing allows you to create a sublist by specifying a range of indices.

    ```python
    print(my_list[1:4])  # Output: [2, 3, 4]
    ```

4. **Modifying Lists**: Lists are mutable, meaning you can modify their elements after creation.

    ```python
    my_list[0] = 10
    print(my_list)  # Output: [10, 2, 3, 4, 5]
    ```

5. **Adding Elements**: You can add elements to a list using methods like `append()`, `insert()`, or concatenation.

    ```python
    my_list.append(6)
    print(my_list)  # Output: [10, 2, 3, 4, 5, 6]
    ```

6. **Removing Elements**: Elements can be removed from a list using methods like `remove()`, `pop()`, or `del`.

    ```python
    my_list.remove(3)
    print(my_list)  # Output: [10, 2, 4, 5, 6]
    ```

7. **List Comprehensions**: List comprehensions provide a concise way to create lists.

    ```python
    squares = [x**2 for x in range(5)]
    print(squares)  # Output: [0, 1, 4, 9, 16]
    ```

8. **Length of a List**: You can find the length of a list using the `len()` function.

    ```python
    print(len(my_list))  # Output: 5
    ```

Lists are fundamental data structures in Python, offering flexibility and efficiency in storing and manipulating collections of items. They are widely used in various programming scenarios, from simple data storage to complex algorithms and data processing tasks.


# Lists are mutable
In Python, lists are mutable, which means you can modify their elements after creation. This is in contrast to immutable data types like strings, where you cannot change individual characters once the string is created.

The syntax for accessing elements of a list is similar to accessing characters of a string—it uses the bracket operator (`[]`). Inside the brackets, you specify the index of the element you want to access. Here's a bit more detail on how this works:

1. **Indexing**: Lists are zero-indexed, meaning the first element is at index 0, the second element is at index 1, and so on. You can use positive indices to access elements from the beginning of the list, and negative indices to access elements from the end of the list.

    ```python
    my_list = [10, 20, 30, 40, 50]
    
    print(my_list[0])  # Output: 10
    print(my_list[2])  # Output: 30
    print(my_list[-1]) # Output: 50 (last element)
    ```

2. **Modifying Elements**: Since lists are mutable, you can change the value of elements using their indices.

    ```python
    my_list[1] = 25
    print(my_list)  # Output: [10, 25, 30, 40, 50]
    ```

3. **Slicing**: You can also use slicing to access multiple elements of a list at once. Slicing allows you to specify a range of indices to retrieve a sublist.

    ```python
    print(my_list[1:4])  # Output: [25, 30, 40]
    ```

4. **Deleting Elements**: You can delete elements from a list using the `del` statement or the `remove()` method.

    ```python
    del my_list[2]
    print(my_list)  # Output: [10, 25, 40, 50]
    ```

    ```python
    my_list.remove(25)
    print(my_list)  # Output: [10, 40, 50]
    ```

The ability to access and modify individual elements of a list using indexing makes lists highly versatile and useful in a wide range of programming scenarios, such as data manipulation, algorithms, and data structures.

# Slicing

In Python, slicing is a powerful technique used to reference a group of elements within a list (or other sequence types) using a range of indices. It allows you to extract a sublist from a larger list based on specified start and end indices. The syntax for slicing is as follows:

```python
new_list = old_list[start:end:step]
```

Here's an explanation of each part of the syntax:

- `old_list`: The original list from which you want to extract elements.
- `start`: The index at which the slice begins (inclusive). If omitted, it defaults to the beginning of the list.
- `end`: The index at which the slice ends (exclusive). If omitted, it defaults to the end of the list.
- `step`: Optional. The step or increment between elements in the slice. If omitted, it defaults to 1.

Here are some examples demonstrating slicing in Python:

1. **Basic Slicing**:

    ```python
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sliced_list = my_list[2:6]
    print(sliced_list)  # Output: [2, 3, 4, 5]
    ```

2. **Slicing with Step**:

    ```python
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sliced_list = my_list[1:9:2]
    print(sliced_list)  # Output: [1, 3, 5, 7]
    ```

3. **Slicing from the Beginning**:

    ```python
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sliced_list = my_list[:5]
    print(sliced_list)  # Output: [0, 1, 2, 3, 4]
    ```

4. **Slicing to the End**:

    ```python
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sliced_list = my_list[5:]
    print(sliced_list)  # Output: [5, 6, 7, 8, 9]
    ```

5. **Negative Indices**:

    ```python
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sliced_list = my_list[-4:-1]
    print(sliced_list)  # Output: [6, 7, 8]
    ```

*Slicing is a versatile tool in Python that allows you to manipulate lists efficiently by selecting subsets of elements based on their indices. It is widely used in various programming scenarios, including data processing, algorithmic tasks, and more.*

# List Methods

In Python, lists come with a variety of built-in methods that allow you to perform various operations on lists efficiently. Here are some commonly used list methods:

1. **append()**: Adds an element to the end of the list.

    ```python
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list)  # Output: [1, 2, 3, 4]
    ```

2. **extend()**: Extends the list by appending elements from an iterable.

    ```python
    my_list = [1, 2, 3]
    my_list.extend([4, 5, 6])
    print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
    ```

3. **insert()**: Inserts an element at a specified position.

    ```python
    my_list = [1, 2, 3]
    my_list.insert(1, 1.5)
    print(my_list)  # Output: [1, 1.5, 2, 3]
    ```

4. **remove()**: Removes the first occurrence of a specified value.

    ```python
    my_list = [1, 2, 3, 2]
    my_list.remove(2)
    print(my_list)  # Output: [1, 3, 2]
    ```

5. **pop()**: Removes the element at a specified position (or the last element if no index is specified) and returns it.

    ```python
    my_list = [1, 2, 3]
    popped_element = my_list.pop(1)
    print(my_list)  # Output: [1, 3]
    print(popped_element)  # Output: 2
    ```

6. **index()**: Returns the index of the first occurrence of a specified value.

    ```python
    my_list = [1, 2, 3, 2]
    index = my_list.index(2)
    print(index)  # Output: 1
    ```

7. **count()**: Returns the number of occurrences of a specified value.

    ```python
    my_list = [1, 2, 3, 2]
    count = my_list.count(2)
    print(count)  # Output: 2
    ```

8. **sort()**: Sorts the list in ascending order (or descending if `reverse=True` is specified).

    ```python
    my_list = [3, 1, 2]
    my_list.sort()
    print(my_list)  # Output: [1, 2, 3]
    ```

9. **reverse()**: Reverses the elements of the list in place.

    ```python
    my_list = [1, 2, 3]
    my_list.reverse()
    print(my_list)  # Output: [3, 2, 1]
    ```

10. **clear()**: Removes all elements from the list.

    ```python
    my_list = [1, 2, 3]
    my_list.clear()
    print(my_list)  # Output: []
    ```

*These methods provide a convenient and efficient way to manipulate lists in Python. They are widely used in various programming tasks involving lists, such as data processing, algorithm implementation, and more.*


# Using for & in

The `for` loop is used to iterate over a sequence (such as a list, tuple, string, or dictionary) or any iterable object. The `in` keyword is used within the `for` loop to specify the sequence or iterable object to iterate over. Here's how `for` and `in` work together in Python:

1. **Iterating Over Lists**:

    ```python
    my_list = [1, 2, 3, 4, 5]
    for element in my_list:
        print(element)
    ```

    Output:
    ```
    1
    2
    3
    4
    5
    ```

2. **Iterating Over Strings**:

    ```python
    my_string = "Hello"
    for char in my_string:
        print(char)
    ```

    Output:
    ```
    H
    e
    l
    l
    o
    ```

3. **Iterating Over a Range of Numbers**:

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

4. **Iterating Over a Dictionary**:

    ```python
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    for key in my_dict:
        print(key, my_dict[key])
    ```

    Output:
    ```
    a 1
    b 2
    c 3
    ```

5. **Using `in` with Conditional Statements**:

    `in` can also be used to check if a value exists in a sequence.

    ```python
    my_list = [1, 2, 3, 4, 5]
    if 3 in my_list:
        print("3 is in the list")
    ```

    Output:
    ```
    3 is in the list
    ```

*`for` loops combined with `in` are fundamental constructs in Python for iterating over sequences and performing various operations on each element. They provide a clean and concise way to work with collections of data.*

# Range

The `range()` function is used to generate a sequence of numbers. It's commonly used with `for` loops to iterate a specific number of times or to generate indices for accessing elements in a sequence. 
- The `range()` function can accept one, two, or three arguments:

1. **`range(stop)`**: Generates numbers from 0 up to, but not including, the specified stop value.

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

2. **`range(start, stop)`**: Generates numbers from the start value up to, but not including, the stop value.

    ```python
    for i in range(2, 6):
        print(i)
    ```

    Output:
    ```
    2
    3
    4
    5
    ```

3. **`range(start, stop, step)`**: Generates numbers from the start value up to, but not including, the stop value, incrementing by the step value.

    ```python
    for i in range(1, 10, 2):
        print(i)
    ```

    Output:
    ```
    1
    3
    5
    7
    9
    ```

*`range()` objects are often used in combination with `for` loops to perform iterative tasks. They're also useful for generating indices when iterating over lists, strings, or other sequences.*

*It's important to note that `range()` itself does not return a list, but rather a range object that behaves like a list of numbers when used in iterations. If you need a list, you can explicitly convert the range to a list using the `list()` function.*

# The while loop

The `while` loop in Python allows you to execute a block of code repeatedly as long as a specified condition is true. It's useful when you don't know in advance how many times you need to execute the loop. Here's the basic syntax of a `while` loop:

```python
while condition:
    # Code block to execute
    # This block will continue to execute as long as the condition is true
```

The `break` and `continue` statements in Python can be used within a `while` loop to alter its behavior:

- `break`: Terminates the loop prematurely when a certain condition is met.
- `continue`: Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.

Here's an example demonstrating the use of a `while` loop in Python:

```python
count = 0
while count < 5:
    print("Count:", count)
    count += 1
```

Output:
```
Count: 0
Count: 1
Count: 2
Count: 3
Count: 4
```

In this example, the `while` loop continues to execute as long as the condition `count < 5` is true. The `count` variable is incremented by 1 in each iteration.

Here's another example using `break` and `continue`:

```python
count = 0
while True:
    count += 1
    if count == 3:
        continue  # Skip printing when count is 3
    print("Count:", count)
    if count == 5:
        break  # Terminate the loop when count reaches 5
```

Output:
```
Count: 1
Count: 2
Count: 4
Count: 5
```

In this example, the loop continues indefinitely (`while True`), but the `continue` statement skips printing when `count` is 3. The loop terminates when `count` reaches 5 due to the `break` statement.


## More examples demonstrating the use of `while` loops with `break` and `continue` statements:

1. **Printing Even Numbers Up to a Limit**:

```python
limit = 10
num = 0
while num <= limit:
    if num % 2 == 0:
        print(num)
    num += 1
```

Output:
```
0
2
4
6
8
10
```

2. **Sum of Numbers Until a Negative Number is Entered**:

```python
total = 0
while True:
    num = int(input("Enter a number (negative to quit): "))
    if num < 0:
        break
    total += num
print("Sum of numbers:", total)
```

3. **Skipping Odd Numbers**:

```python
num = 0
while num < 10:
    num += 1
    if num % 2 != 0:
        continue
    print(num)
```

Output:
```
2
4
6
8
10
```

4. **Password Validation** (Terminates after 3 failed attempts):

```python
password = "secret"
attempts = 0
while attempts < 3:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Access granted!")
        break
    else:
        print("Invalid password. Try again.")
        attempts += 1
else:
    print("Too many failed attempts. Access denied.")
```

*These examples illustrate different scenarios where `while` loops, along with `break` and `continue` statements, provide flexibility and control flow in Python programs.*



# List Methods
### Let's expand on each of the mentioned list methods with examples:

1. **`append(elem)`**: Adds a single element to the end of the list.

    ```python
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list)  # Output: [1, 2, 3, 4]
    ```

2. **`insert(index, elem)`**: Inserts the element at the given index, shifting elements to the right.

    ```python
    my_list = [1, 2, 4]
    my_list.insert(2, 3)
    print(my_list)  # Output: [1, 2, 3, 4]
    ```

3. **`extend(list2)`**: Adds the elements in `list2` to the end of the list.

    ```python
    my_list = [1, 2, 3]
    my_list.extend([4, 5])
    print(my_list)  # Output: [1, 2, 3, 4, 5]
    ```

4. **`index(elem)`**: Searches for the given element from the start of the list and returns its index. Throws a `ValueError` if the element does not appear.

    ```python
    my_list = [1, 2, 3, 4, 5]
    index = my_list.index(3)
    print(index)  # Output: 2
    ```

5. **`remove(elem)`**: Searches for the first instance of the given element and removes it. Throws a `ValueError` if not present.

    ```python
    my_list = [1, 2, 3, 4, 5]
    my_list.remove(3)
    print(my_list)  # Output: [1, 2, 4, 5]
    ```

6. **`sort()`**: Sorts the list in place. 

    ```python
    my_list = [3, 1, 4, 2, 5]
    my_list.sort()
    print(my_list)  # Output: [1, 2, 3, 4, 5]
    ```

7. **`reverse()`**: Reverses the list in place.

    ```python
    my_list = [1, 2, 3]
    my_list.reverse()
    print(my_list)  # Output: [3, 2, 1]
    ```

8. **`pop(index)`**: Removes and returns the element at the given index. Returns the rightmost element if index is omitted.

    ```python
    my_list = [1, 2, 3, 4, 5]
    popped_element = my_list.pop(2)
    print(popped_element)  # Output: 3
    print(my_list)  # Output: [1, 2, 4, 5]
    ```

*These methods provide powerful tools for manipulating lists in Python, allowing you to add, remove, sort, and modify elements based on various criteria.*


# List comprehension 

List comprehension is a *concise and efficient way to create lists in Python*. It allows you to generate lists using a single line of code by applying an expression to each item in an iterable object. List comprehension offers a more readable and expressive way to write loops compared to traditional looping constructs.

Here's the basic syntax of list comprehension:

```python
new_list = [expression for item in iterable if condition]
```

- `expression`: The expression to be evaluated for each item in the iterable.
- `item`: The variable representing each item in the iterable.
- `iterable`: The iterable object (e.g., list, tuple, string, etc.) that the loop iterates over.
- `condition` (optional): A condition that filters the elements. The expression is only evaluated if the condition is `True`.

Let's expand on list comprehension with examples:

1. **Generating Squares of Numbers**:

```python
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

2. **Filtering Even Numbers**:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
```

3. **Converting Temperatures from Celsius to Fahrenheit**:

```python
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = [(9/5) * temp + 32 for temp in celsius_temps]
print(fahrenheit_temps)  # Output: [32.0, 50.0, 68.0, 86.0, 104.0]
```

4. **Flattening a 2D List**:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

*List comprehension allows you to write clear and concise code, making it easier to express complex operations on lists in a single line. It's a powerful tool in Python programming, and mastering it can greatly improve your coding efficiency and readability. Practice using list comprehension in various scenarios to become more proficient in its usage.*

# The `sorted()` function and the `sort()` method

Let's cover the sorting of lists, both with the `sorted()` function and the `sort()` method. We'll also discuss tuples in Python.

### Sorting Lists

#### Using `sorted()` Function
The `sorted()` function sorts a list without modifying the original list. It returns a new sorted list.

Example:

```python
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = sorted(my_list)
print(sorted_list)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

#### Using `sort()` Method
The `sort()` method sorts the list in place, modifying the original list. It does not return a new list.

Example:

```python
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
my_list.sort()
print(my_list)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

### Custom Sorting with `key=`

The `key` parameter in both `sorted()` function and `sort()` method allows custom sorting based on a function that transforms each element before comparison.

Example:

```python
my_list = ["apple", "banana", "cherry", "date", "elderberry"]
custom_sorted_list = sorted(my_list, key=len)
print(custom_sorted_list)  # Output: ['date', 'apple', 'banana', 'cherry', 'elderberry']
```

This sorts the list based on the length of each string.

### Tuples

A tuple is an immutable sequence of elements, typically used to store collections of heterogeneous data. Once a tuple is created, its elements cannot be changed or added. Tuples are defined using parentheses `()`.

Example:

```python
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)
```

Tuples are often used to represent fixed collections of items, like coordinates or data records. They support operations like indexing, slicing, and iteration, similar to lists.

```python
coordinates = (3, 4)
x, y = coordinates
print("x-coordinate:", x)  # Output: x-coordinate: 3
print("y-coordinate:", y)  # Output: y-coordinate: 4
```

Tuples are also commonly returned by functions to represent multiple values returned together.

```python
def get_coordinates():
    return (3, 4)

coordinates = get_coordinates()
print(coordinates)  # Output: (3, 4)
```

Tuples are immutable, meaning their elements cannot be changed after creation, making them suitable for situations where you want to ensure data integrity or prevent accidental modification.

