# the basic while sentence
count = 0
print('\n','the basic')

while count < 5:
    print(count)
    count += 1

# use break point and continue
count = 0
print('\n','break point and continue')

while True:
    # you completely leave the while sentence
    if count >= 5:
        break
    # you skip one and continue the while sentence
    if count == 2:
        count += 1
        continue
    print(count)
    count += 1

# process to the end and swich to else
count = 0
print('\n','while else')
while count < 5:
    print(count)
    count += 1
else:
    print('done')

# if you break the sentence,
# you can not swich to else
count = 0
print('\n','if use break point')
while count < 5:
    print(count)
    if count == 2:
        break
    count += 1
else:
    print('done')


