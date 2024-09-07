
class Human:
   def __init__(self, name, age, height):
       self.name = name
       self.age = age
       self.height = height


   def __str__(self):
       return f"object class Human, name {self.name}"


   def __int__(self):
       return self.age


   def say_hi(self):
       print(f'hello my name is {self.name}! Im {self.age} years old and my height is {self.height}')


class Auto:
    def __init__(self, brand, max_passengers = 5):
        self.brand = brand
        self.max = max_passengers
        self.passengers = []


    def add_passengers(self, *new_passengers):
        for passenger in new_passengers:
            if len(self.passengers) >= self.max:
                print('auto is full')
            else:
                self.passengers.append(passenger)

    def print_all_passengers(self):
        if len(self.passengers) == 0:
            print(f'Auto {self.brand} is empty')
        else:
            print(f'passengers in {self.brand}:')
            for i in self.passengers:
                i.say_hi()



bob = Human('bob', 18, 181.1)
alice = Human('alice', 16, 175)
tolik = Human('Tolik', 35, 165)
vasya = Human("vasya", 12, 152)
petro = Human('petro', 16, 179)
anna = Human('anna', 19, 189)


bmw = Auto('BMW')
tesla = Auto("Tesla")

tesla.add_passengers(bob, alice, tolik, vasya, petro)

tesla.print_all_passengers()
bmw.print_all_passengers()

