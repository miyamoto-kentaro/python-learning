# if you use package when an error is like to occur
try:
    from lesson_package import utils
except ImportError:
    from lesson_package.tools import utils

print(utils.say_twice('word'))