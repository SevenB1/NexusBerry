class Car:
    def __init__(self,make,model,mileage,fuel):
        self.make = make
        self.model = model
        self._mileage = mileage
        self.__fuel = fuel

    def display_info(self):
        print(f'This is {self.make} {self.model}')
    def show_mileage(self):
        print(f'Mileage: {self._mileage} miles')
    def __update_fuel(self,amount):
        self.__fuel = amount
        print(f'Fuel Updated to {self.__fuel} gallons')
    def accessUpdate_fuel(self,amount):
        self.__update_fuel(amount)

class HybridCar(Car):
    def __init__(self,make,model,mileage,fuel,battery_life):
        super().__init__(make,model,mileage,fuel)
        self._battery_life = battery_life
    def show_battery_life(self):
        print(f'Battery Life: {self._battery_life} KWh')
    def display_car_info(self):
        self.display_info()
        self.show_mileage()
        self.accessUpdate_fuel(20)
        self.show_battery_life()


# my_car = Car("Toyota","Corolla GLI",5000,10)
# my_car.display_info()
# my_car.show_mileage()

hybrid_car = HybridCar("Toyota","Prius",3000,20,6)
hybrid_car.display_car_info()

#Mini Project OOP
#Course Registration
#class Student
#Attributes: reg_no, name
#methods: list_all_courses(), course_add(),course_drop(),list_registered_courses()
#Course
#Attributes: Course_code, course_title, course_credit_hours
#Registration
#add_course()