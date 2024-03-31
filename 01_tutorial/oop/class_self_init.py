class Car():
    
    # exercise 6
    # static variable to count the no of cars made
    total_cars_made = 0

    # exericse 7
    # static method to describe the overview of Car class
    @staticmethod   # @ -> Decorators  
    def general_description():
        return 'Cars are means of transport'

    # constructor
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars_made += 1
    
    def get_brand(self):
        return self.__brand 

    def set_brand(self):
        pass

    @property       # exercise 8
    def model(self):
        return self.__model

    # polymorphism
    def fuel_type(self):
        return 'petrol or diesel'


    def display_name(self):
        return f'The car brand is {self.__brand} and model is {self.__model}'

# # exercise 1
# tata_harrier = Car('Tata', 'Harrier')
# print(tata_harrier.display_name(), tata_harrier.get_brand(), tata_harrier.fuel_type())

# # exercise 2
# print(tata_harrier.display_name())