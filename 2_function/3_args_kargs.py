# we sometime want to use some arguments
# but if we don't know how many arguments we have, we should use *args
def arguments(*args):
    print(args)
    for arg in args:
        print(arg)

arguments('Hi','Mike','How are you?')

# if you want to use dictionary args, you use arguments like this
def keyargs(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert':'ice'
}

keyargs(**d)

# we usable normal argument
def mixed(word,*args):
    print('word= ',word)
    for arg in args:
        print(arg)

# 'Hi' is word, ('Mike','How are you?') is *args
mixed('Hi','Mike','How are you?')