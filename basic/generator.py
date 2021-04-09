# Determine if the function
# performed the process and then run the function
def counter(num=10):
    for i in range(num):
        yield i

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'


g = greeting()
c = counter()
print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))