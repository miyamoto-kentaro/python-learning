some_list = [1,2,3,4,5]

# the basic sentence
for i in some_list:
    print(i)

# we can enter the character strings in order
for i in 'abcdef':
    print(i)

# we can enter the character list in order
for word in ['My', 'name', 'is', 'Mike']:
    print(word)

# we can use else sentence
for fruit in ['apple','banana','orange']:
    print(fruit)
else:
    print('I ate all')

# if we also use break
# we can not run else processing
for fruit in ['apple','banana','orange']:
    if fruit == 'orange':
        break
    print(fruit)
else:
    print('I ate all')
    