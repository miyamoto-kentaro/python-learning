# use at saving without executing function
def outer(a,b):
    """Returnning function
    
    Args:
    (explanation of argments)
        a(int): The first integer. 
        b(int): The second integer

    Returns:
    (explanation of returns)
        function: The return function.
        returnning function is un executing
    """

    def inner():
        return a + b
    
    return inner

f = outer(1,2)

print(f)

r = f()
print(r)

# for example
def circle_area_func(pi):
    """Return function that can be return
    circle area with any pi

    Args:
    (explanation of argments)
        pi(float): The first real number.

    Returns:
    (explanation of returns)
        function: The return function.
        returnning function is un executing
    """
    def circle_area(radius):
        return pi * radius * radius
    
    return circle_area

cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.121592)

print(cal1(10))
print(cal2(10))
