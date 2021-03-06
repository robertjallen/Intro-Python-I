"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
# with open('src/foo.txt') as f:
# # foo = open('foo.txt')
#   print(f.read())
#   f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE


# y = open("src/bar.txt", "w")
# y.write("this is first line.\n")
# y.write("this is second line.\n")
# y.write("this is third line.\n")
# y.write("this is fourth line.")
# y.close()
# with open("src/bar.txt") as y:
#   print("\n" + y.read())

# YOUR CODE HERE


new_line = "This new line will be added.\n"

with open("src/bar.txt", "a") as a_file:
  a_file.write("\n")
  a_file.write(new_line)



# add_line()