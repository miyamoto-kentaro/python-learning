# if we want to use some word, we can also use some variable
def say_something(word,word2,word3):
    print(word)
    print(word2)
    print(word3)

say_something('Hi!','Mike','How are you?')

# but we can also use one variable called args
# it hold tuple

def say_something2(*args):
    print(args)
    for arg in args:
        print(arg)

say_something2('Hi','Mike','How are you?')

# we van also be mixed with regular variables

def say_something3(word2,*args):
    print('word= ',word2)
    for arg in args:
        print(arg)

say_something3('Hi','Mike','How are you?')