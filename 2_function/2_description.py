# it grammar to write function
# we should add description to function like this
def sample_func(param1,param2):
    """description of function
    
    Args:
    (description of argments)
        param1(int): The first parameter. 
        param2(str): The second parameter

    Returns:
    (description of returns)
        bool: The return value. True for success, False otherwise
    """
    print(param1)
    print(param2)
    return True

sample_func(12,'Mike')

# we can look description like this
# help function return comment from function
help(sample_func)
# exit this help to command [:q]