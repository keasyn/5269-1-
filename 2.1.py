import random


class Human:
    def __init__(self, name="Human", job=None, house=None, car=None):
        self.name = name
        self.job = job
        self.house = house
        self.car = car

        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def get_job(self):
        self.job = Job(jobs)
        print(f'{self.name} is a {self.job.job_name} now!')

    def get_house(self):
        self.house = House()
        print(f'{self.name} got a house!')

    def get_car(self):
        self.car = Auto(cars)
        print(f'{self.name} got a {self.car.brand}!')

    def work(self):
        if not self.car.drive():
            if self.car.fuel < self.car.consumption:
                self.shopping('fuel')
            else:
                self.to_repair()
            return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def eat(self):
        if self.house.food <= 0:
            self.shopping('food')
        else:
            self.satiety += 5
            self.house.food -= 5

            if self.satiety > 100:
                self.satiety = 100


    def shopping(self, manage):
        if manage == 'fuel':
            print(f'{self.name} buys fuel')
            self.money -= 100
            self.car.fuel += 100
        if manage == 'food':
            print(f'{self.name} buys food')
            self.money -= 50
            self.house.food += 50
        if manage == 'delicious':
            print(f'{self.name} went to the restaurant!')
            self.money -= 100
            self.satiety += 20
            self.gladness += 10
            if self.satiety > 100:
                self.satiety = 100


    def chill(self):
        self.gladness += 10
        self.house.mess += 5


    def clean_house(self):
        self.gladness -= 5
        self.house.mess = 0


    def to_repair(self):
        self.money -= 500
        self.car.strength += 50


    def day_indexes(self, day):
        print(f'----==== Today is {day} day of {self.name}`s life ====----')
        print(f'---=== {self.name}`s happiness: {self.gladness}, money: {self.money} satiety: {self.satiety} ===---')
        print(f'--== {self.name}`s car has {self.car.fuel} liters of fuel in it and has {self.car.strength} times to ride left ==--')
    def is_alive(self):
        if self.gladness < 0:
            print(f'{self.name}`s committed suicide')
            return False
        if self.money <= -500:
            print(f'{self.name} got killed by collectors')
            return False
        if self.satiety < 0:
            print(f'{self.name} died from a hunger')
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False

        if self.house is None:
            self.get_house()
        if self.car is None:
            self.get_car()
        if self.job is None:
            self.get_job()

        self.day_indexes(day)

        if self.satiety < 20:
            self.eat()
        if self.house.mess > 20:
            self.clean_house()

        dice = random.randint(1, 4)

        if dice == 1:
            print(f'{self.name} went to the work')
            self.work()
        elif dice == 2:
            print(f'{self.name} decided to chill')
            self.chill()
        elif dice == 3:
            print(f'{self.name} cleaned the house')
            self.clean_house()
        elif dice == 4:
            self.shopping('delicious')


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, jobs_dict):
        self.job_name = random.choice(list(jobs_dict))
        self.salary = jobs_dict[self.job_name]['salary']
        self.gladness_less = jobs_dict[self.job_name]['gladness_less']


class Auto:
    def __init__(self, cars_dict):
        self.brand = random.choice(list(cars_dict))
        self.fuel = cars_dict[self.brand]['fuel']
        self.strength = cars_dict[self.brand]['strength']
        self.consumption = cars_dict[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and (self.consumption <= self.fuel):
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('Oops! Auto is not drivable')
            return False



cars = {
    'Bmw':{
        'fuel':100,
        'strength':25,
        'consumption':15
    },
    'Hyundai':{
        'fuel':80,
        'strength':30,
        'consumption':10
    },
    'Audi':{
        'fuel':110,
        'strength':35,
        'consumption':10
    },
    'Porsche':{
        'fuel':120,
        'strength':40,
        'consumption':30
    },
    'Ferrari':{
        'fuel':130,
        'strength':40,
        'consumption':35
    }
}
jobs = {
    'Jobless':{
        'salary':5,
        'gladness_less':50
    },
    'Cleaner':{
        'salary':150,
        'gladness_less':25
    },
    'Teacher':{
        'salary':170,
        'gladness_less':5
    },
    'Doctor':{
        'salary':250,
        'gladness_less':15
    },
    'Junior Python developer':{
        'salary':900,
        'gladness_less':11
    },
    'Senior Python developer':{
        'salary':3000,
        'gladness_less':3
    },
    'Successful businessman':{
        'salary':30000,
        'gladness_less':1
    }
}

bobos = Human("Bobos")

for day in range(1, 10001):
    if not bobos.is_alive():
        break
    else:
        bobos.live(day)
print(bobos.job.job_name)
