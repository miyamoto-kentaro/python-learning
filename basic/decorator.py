# use at processing before and after the function

def print_info(func):
    """decorator function have used function argment.
    case of we want to add any processing before and after the running function
    
    Args:
    (explanation of argments)
        func(function): function to want to run

    Returns:
    (explanation of returns)
        function: the return function adding any processing.
    """
    def wrapper(*args,**kwargs):
        print('start')
        result = func(*args,**kwargs)
        print('end')
        return result
    return wrapper

def print_more(func):
    def wrapper(*args,**kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args,**kwargs)
        print('result:', result)
        return result
    return wrapper

# @print_info
# @print_more
# def add_num(a,b):
#     return a + b

# r = add_num(10,20)
# print(r)

@print_info
@print_more
def sub_num(a,b):
    return a - b

r = sub_num(20,10)

# r = sub_num(10,20)
# print(r)

# f = print_info(add_num)
# r = f(10,20)
# print(r)