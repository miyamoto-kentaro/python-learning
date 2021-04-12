# use at argment is smart function
l = ['Mon','tue', 'Wed', 'Thu', 'fri', 'sat', 'sun']

def change_words(words, func):
    for word in words:
        print(func(word))

change_words(l, lambda word: word.capitalize())
"""lambda function process to return changed word
argument
"""