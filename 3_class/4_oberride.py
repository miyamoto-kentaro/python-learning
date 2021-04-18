# Inherited class that has constractor
class Car(object):
    # self object is the parent
    def __init__(self, model=None):
        self.model = model
    def run(self):
        # if quote model with out model, cannot call model
        print(self.model,'is runing')

# we can oberride the function like this
class ToyotaCar(Car):
    def run(self):
        print(self.model,'is fast')

# we can update to use super() function
class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        super().__init__(model)
        # it's additional process
        self.enable_auto_run = enable_auto_run
    def run(self):
        print(self.model,'is super fast')
    def auto_run(self):
        print('auto run')

car = Car()
car.run()
print('##############')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()
print('##############')
tesla_car = TeslaCar('Model S')
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()