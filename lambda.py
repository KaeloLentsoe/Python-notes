#Lambda expressions, also known as lambda functions, in python.
# Lambda syntex:-
# lambda  parameter: expression

#Regular function
def add(x, y):
    return x + y

# Equivalent lambda expression 
add_lambda = lambda x, y: x + y

# Using the lambda function
result = add_lambda(3, 4)
print(result) #Output: 7

