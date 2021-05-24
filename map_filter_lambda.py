"""A map() function is used to connect a function with an input. Usually used with functions containing a calculation
and returning/printing the result for something like a List for an input. It will map the calculation inside the
function to all the numbers in the input list.

A filter() function works similar to a map() function, but usually used with functions containing a condition.
It will check the condition inside the function for all elements of an input like a List. Then return the result accordingly.

A lambda expression is used to create anonymous functions without a definition or a name.
Typically for a one-time use in conjunction with map() or filter().
"""


# defining a function that returns the square of a number:
def print_square(num):
    return num ** 2


myList = [1, 2, 3, 4, 5]
map(print_square, myList)

# We can either convert the map() output into a list or iterate through it:
result1 = list(map(print_square, myList))
print(result1)

for x in map(print_square, myList):
    print(x)
print('\n')


# defining a function that checks if a number is even or not:
def check_even(num):
    return num % 2 == 0


filter(check_even, myList)

# Again, we need to convert it into a list or iterate through it:
result2 = list(filter(check_even, myList))
print(result2)

for n in filter(check_even, myList):
    print(n)
print('\n')

# If we use a lambda function, we do not even have to define the functions above:

result3 = list(map(lambda num: num ** 2, myList))
print(result3)
print('\n')

result4 = list(filter(lambda num: num % 2 == 0, myList))
print(result4)
print('\n')
