# object class has property instance
# Inherited class
class Car(object):
    def run(self):
        print('run')
# inherits class
class ToyotaCar(Car):
    pass


class TeslaCar(Car):
    def auto_run(self):
        print('auto run')

# Create object
car = Car()
# call back function name instance
car.run()
print('#'*10)
toyota_car = ToyotaCar()
toyota_car.run()
print('#'*10)
tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()