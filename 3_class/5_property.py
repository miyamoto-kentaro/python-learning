class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S',
    enable_auto_run=False,
    passwd='123'):
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run
        self.passwd = passwd

    # we use property if variables become read only
    @property
    def enable_auto_run(self):
        return self.__enable_auto_run
    
    # we use setter if variables seted any
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self.__enable_auto_run = is_enable
        else:
            raise ValueError    

    def run(self):
        print(self.__enable_auto_run)
        print('super fast')

    def auto_run(self):
        print('auto run')

tesla_car = TeslaCar('Model S',passwd='456')
tesla_car.enable_auto_run = True
# print(tesla_car.__enable_auto_run)
print(tesla_car.enable_auto_run)