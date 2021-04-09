class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE','orange','banana']
    for word in words:
        if word.isupper:
            raise UppercaseError(word)

check()