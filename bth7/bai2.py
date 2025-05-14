class Vihecle:
    def __init__(self,make) :
        self.make=make
    
    def description():
        pass

class Car(Vihecle):
    def __init__(self, make,model):
        super().__init__(make)
        self.model=model

    def description(self):
        print(self.make," ",self.model)

class ElectricCar(Car):
    def __init__(self, make, model,battery_size):
        super().__init__(make, model)
        self.battery_size=battery_size

    def description(self):
        print(self.make," ",self.model," ",self.battery_size)

a= Car("1" , "Elae")
b= ElectricCar("2","Tesla","33")
a.description()
b.description()