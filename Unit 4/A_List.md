# Indexing

Indexing in Python typically refers to accessing individual elements within a data structure like **lists, tuples, strings, or dictionaries.* Each element in such data structures is assigned a unique index, starting from 0 for the first element, 1 for the second, and so on.

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