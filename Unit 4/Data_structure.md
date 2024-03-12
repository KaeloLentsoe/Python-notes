# Unit 4: Data Structures I – Lists and Strings

- In this unit, we explore how data is structured within Python so we can program efficiently. 

- Specifically, you will be introduced to lists and also immersed more deeply in the subject of strings. Upcoming units will introduce even more powerful data structures.

# 4.1 Python Lists
## Creating Lists

Definition of a list: 
**"A list is a data structure capable of storing different types of data."**

In Python, **a list is a built-in data structure that allows you to store and organize a collection of items.** Lists are mutable, which means you can change their **elements** by adding, removing, or modifying items. Lists are defined by enclosing the elements in square brackets `[]` and separating them with commas.

Here's the basic syntax for creating a list in Python:

```python
my_list = [element1, element2, element3, ...]
```

- `my_list`: The name of the list.
- `element1`, `element2`, `element3`, ...: The individual elements of the list. These can be of any data type, and you can mix different types within the same list.

Here's an example of creating a simple list:

```python
fruits = ["apple", "banana", "orange", "grape"]
```

In this example, the list `fruits` contains strings representing different types of fruits.

**Lists in Python are versatile and can be used for various purposes, such as storing collections of numbers, strings, or even other lists. They are commonly used for tasks like iteration, data manipulation, and storage of heterogeneous data.*


# Data elements

In Python, the data elements stored within a list are called elements. Each element in a list can be of any data type, including integers, floats, strings, booleans, or even other complex data structures like other lists. Here's a bit more detail:

1. **Data Types:**
   - Elements in a list can be of different data types. For example, a single list might contain a combination of integers, strings, and booleans.

   ```python
   mixed_list = [42, "hello", 3.14, True]
   ```

2. **Accessing Elements:**
   - You can access individual elements in a list using indexing. Python uses zero-based indexing, meaning the first element is accessed with index `0`, the second with index `1`, and so on.

   ```python
   my_list = ["apple", "banana", "orange"]
   print(my_list[0])  # Output: "apple"
   ```

3. **Mutability:**
   - Lists in Python are mutable, which means you can modify them by adding, removing, or changing elements after the list is created.

   ```python
   my_list = [1, 2, 3]
   my_list[1] = 4
   print(my_list)  # Output: [1, 4, 3]
   ```

4. **Length of a List:**
   - You can find the number of elements in a list using the `len()` function.

   ```python
   my_list = [10, 20, 30, 40, 50]
   print(len(my_list))  # Output: 5
   ```

5. **Slicing:**
   - Lists support slicing, allowing you to extract portions of the list.

   ```python
   numbers = [1, 2, 3, 4, 5]
   sliced_list = numbers[1:4]
   print(sliced_list)  # Output: [2, 3, 4]
   ```

Understanding these aspects of lists in Python is crucial for effectively working with data and performing various operations on collections of elements.