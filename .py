# Makes a class called Car that takes model type, color, mpg and condition into account
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
       return "This is a " + self.color + " " +  self.model + " with " +  str(self.mpg) + " MPG."
    # Changes the condition of the car if this method is utilized.
    def drive_car(self):
        self.condition = "used"
my_car = Car("DeLorean", "silver", 88)
print my_car.condition
my_car.drive_car()
print my_car.condition

# Similar class as Car, but gathers the same information for an electric car
class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type = battery_type
    def drive_car(self):
        self.condition = "like new"
my_car = ElectricCar("Ford", "Green", 45, "molten salt")    
print my_car.condition
my_car.drive_car()
print my_car.condition
        
