# use at we want to turn dictionary argment,
# we can use **kwargs argments
def menu(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert':'ice'
}

menu(**d)