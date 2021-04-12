# use at you want to execute multiple values
days = ['Mon','Tue','Wed']
fruits = ['apple','banana','orange']
drinks = ['coffee','tea','beer']

for day,fruit,drink in zip(days,fruits,drinks):
    print(day, fruit, drink)