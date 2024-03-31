from class_self_init import Car

class Electric_car(Car):
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        # inheritance
        super().__init__(brand, model)
    
    # polymorphism
    def fuel_type(self):
        return 'electric charge'

ec1 = Electric_car('tesla', 'model-x', '1000KVh')
normal = Car('Tata', 'Harrier')

# print(ec1.display_name(),'battery size=', ec1.battery_size, ec1.fuel_type())

# print(ec1.total_cars_made)  # Wrong
# print(Car.total_cars_made)  # Correct

# exercise 7
# static method calling
# # print(ec1.general_description())          # Wrong
# print(Electric_car.general_description())   # Correct
# print(Car.general_description())            # Correct

# exercise 8
# READ ONLY property
# normal.model = 'Nexon'  # can't change the model property because it is 
# print(normal.model)       # read only

# exercise 9
# my_tesla = Electric_car('tesla', 'model-y', '2000KVh')
# print(isinstance(my_tesla, Car), isinstance(my_tesla, Electric_car))

# exercise 10
class Battery:
    def battery_info(self):
        return 'this is battery'

class Engine:
    def engine_info(self):
        return 'This is engine'
    
class Electric_car_2(Battery, Engine, Car):
    pass

my_tesla2 = Electric_car_2('tesla', 'model-z')

print(my_tesla2.battery_info(), my_tesla2.engine_info())    # hence prooved