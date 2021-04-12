animal = 'cat'

def f():
    global animal
    # animal = 'dog'
    print('locals:',animal)

def f2():
    animal = 'rabit'
    print('local2',animal)

def f3():
    global animal
    animal = 'dog'
    print('locals3:',animal)

f()
f2()
f3()
print('global:',animal)