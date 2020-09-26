# Print out each element of the following array on a separate line:

# x = ['Joe', 2, 'Ted', 4.98, 14, 'Sam', 'void *', '42', 'float', 'pointers', 5006]

# for item in x:
#   print(item)





# Verbalize your thought process as much as possible before writing any code.
# Run through the UPER problem solving framework while going through your thought process.

# # Print out each element of the following array on a separate line, but this time the 
# input array can contain arrays nested to an arbitrarily deep level:
# ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]
# For the above input, the expected output is:
# Bob
# Slack
# reddit
# 89
# 101
# alacritty
# (brackets)
# 5
# 375
# 0
# {slice, owned}
# 22

x = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

for item in x:
  if type(item) == str:
    print(item)
  elif type(item) == list:
    for i in item:
      if type(i) == str:
        print(i)
      elif type(i) == list:
        for x in i:
          print(x)
  elif type(item) == int:
    print(item)             


