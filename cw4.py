# class Cat:
# def __init__(self, name, age):
#  self.name = name
#   self.age = age
#    self.countlife = 9

# def show_info(self):
# print (f"Name: {self.name}")
# print (f"Age: {self.age}")
# print(f"Count life:{self.countlife}")
# class Dog:
#   def __init__(self, name, age):
#      self.name = name
#     self.age = age

# def show_info(self):
#   print(f"Name: {self.name}")
#  print(f"Age: {self.age}")

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def golos(self):
        pass


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.countLife = 9

    def show_info(self):
        super().show_info()
        print("Count life:", self.countLife)

    def golos(self):
        print("meow-meow")


cat = Cat("barsik", 10)
cat.show_info()


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def show_info(self):

        super().show_info()
    def golos(self):
        print("gow-gow")

dog = Dog("scobee", 15)
dog.show_info()


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Pilot(Human):
    def __init__(self, name, age):
        super().__init__(name, age)

    def show_info(self):
        super().show_info()
        print("I'm controling Boeing 747")

pilot = Pilot("Jeffrey", 35)
pilot.show_info()



