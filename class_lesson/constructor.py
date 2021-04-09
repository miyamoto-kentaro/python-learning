class Person(object):
    def __init__(self, name='Jone'):
        self.name = name
        print('First')
        print(self.name)

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run()
    
    def run(self):
        print('run')
    
    def __del__(self):
        print('good bye')


person = Person('Mike')
person.say_something()
del person
print('####')