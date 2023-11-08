# #Two types of programming paradiagm
# #i)Structured programming(modular programming)
# #ii)Object Oriented Programming in Python(real life objects)
# #Class -- template -- Attributes and behavior
# #Class Car, Attribute-- (engine power, make, 2wd, 4wd, gears)
# #Behavior-- Start(), run(), turn(), stop(), reverse()
# #create objects -> car object -- set the attributes values
# #e.g class student--> id, name, semester, CGPA, undergrad, graduate
# #behavior of student object -> study(), give_exam(), participate_extra_curricular()
# #e.g class Employee --> id, name, designation, project_name, salary etc..
# #behavior--> work(), overtime(), leave()
# #Behavior--functions

# class Myclass:
#     x = 5
# myobj = Myclass() #constructor
# print("My First Object oriented lecture, printing the object attribute", myobj.x)

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Person('Ahmad',36)
# p2 = Person('Zahid',42)
# print(f'Name of first person is {p1.name} and age is {p1.age}')
# print(f'Name of second person is {p2.name} and age is {p2.age}')


# class Account:
#     def __init__(self,balance,acc_no):
#         print("init() method is called ")
#         self.acc_no = acc_no
#         self.balance = balance

#     def __str__(self):
#         return f'Account Number ={self.acc_no} and Balance = {self.balance}'

#     def withdraw(self,amount):
#         print(f'Account Number {self.acc_no} and its Balance is{self.balance}')
#         print("Withdrawal amount ",amount)
#         self.balance = self.balance - amount
#     def deposit(self,amount):
#         print(f'Account Number {self.acc_no} and its Balance is{self.balance}')
#         print("Depsit amount ", amount)
#         self.balance = self.balance + amount



# acc1 = Account(5000,'Acc001')
# acc2 = Account(3000,'Acc002')

# print(acc1)
# print(acc2)
# # print(f'Account no is {acc1.acc_no} and its balance is {acc1.balance}')
# # print(f'Account no is {acc2.acc_no} and its balance is {acc2.balance}')

# acc1.withdraw(2000)
# print(f'Account no is {acc1.acc_no} and its balance is {acc1.balance}')
# acc2.withdraw(1000)
# print(f'Account no is {acc2.acc_no} and its balance is {acc2.balance}')

# acc1.deposit(4000)
# print(f'Account no is {acc1.acc_no} and its balance is {acc1.balance}')

# acc2.deposit(6000)
# print(f'Account no is {acc2.acc_no} and its balance is {acc2.balance}')

# #Subclass or Inherited Class or Derived class or Child class
# class Animal: #Acts as a parent class
#     def eat(self):
#         print("I can eat")
#     def sleep(self):
#         print("I can sleep")
# #Derived Class
# class Dog(Animal):
#     def bark(self):
#         print("I can Bark Woof Woof")

# dog1 = Dog()
# dog1.eat()
# dog1.sleep()
# dog1.bark()

class Vehicle:
    def __init__(self,make,color,engine_power,reg_no):
        self.make = make
        self.color = color
        self.enginer_power = engine_power
        self.reg_no = reg_no
    def __str__(self):
        return f'Make={self.make},Color={self.color},Engine_Power={self.engine_power},Reg_no={self.reg_no}'


class Car(Vehicle):
        def __init__(self,make,color,engine_power,reg_no,num_doors):
            super().__init__(make,color,engine_power,reg_no)
            self.num_doors = num_doors


class Bus(Vehicle):
    def __init__(self, make, color, engine_power, reg_no, num_passengers):
        super().__init__(make, color, engine_power, reg_no)
        self.num_passengers = num_passengers

class Truck(Vehicle):
        def __init__(self, make, color, engine_power, reg_no, max_load):
            super().__init__(make, color, engine_power, reg_no)
            self.max_load = max_load

car = Car("Toyota","Blue","1800","2022",4)
bus = Bus("Volvo","Orange","4000","2023",40)
truck = Truck("Ford","Black","3500","2020",5000)

print(f'Car Make {car.make} number of doors {car.num_doors}')
print(f'Bus Make {bus.make} number of passengers {bus.num_passengers}')
print(f'Truck Make {truck.make} maximum load {truck.max_load}')