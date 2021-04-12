# use at funning short process in genarator
def g():
    for i in range(10):
        yield i

g = g()
print(type(g))

g = (i for i in range(10) if not i%2)
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
