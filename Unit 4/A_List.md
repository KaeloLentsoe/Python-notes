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