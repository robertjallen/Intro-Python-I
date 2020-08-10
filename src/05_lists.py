# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
# x.extend(y)
# print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
print(x + y[1:])

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE

last_y = y[1:]
last_y_extra = last_y.insert(1, 99)
print(x + last_y)


# Print the length of list x
# YOUR CODE HERE

length = len(x)
print(length)

# Print all the values in x multiplied by 1000
# YOUR CODE HERE

for i in x:
  print(i*1000)


  