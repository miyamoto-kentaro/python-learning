is_empty = None

# print(help(is_empty))

# we can also use is
# is discriminat to determine object
if is_empty is None:
    print('None!!')
else:
    print('empty!')

# this is wornning
if 1 is None:
    print("It's None object")
else:
    print("It's not None object")