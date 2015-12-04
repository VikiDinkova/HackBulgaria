from random import randint


class Car:
    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        return "{} {} with max speed of: {}".format(self.car, self.model, self.max_speed)

    def __int__(self):
        return int(self.max_speed)


class Driver:
    def __init__(self, name, car):
        self.name = name
        self.car = car

    def __str__(self):
        return "{} drives {} {}".format(self.name, self.car.car, self.car.model)


class Race():
    def __init__(self, drivers, crash_chance):
        self.drivers = [driver.name for driver in drivers]
        self.crash_chance = crash_chance
        self.crashed = False

    def crash(self):
        num = randint(1, 10)
        if self.crash_chance * num > 5:
            self.crashed = True
            print("Unfortunately, {} has crashed.".format(self.drivers.name))

    def result(self):
        result = []
        a, b, c, d = self.drivers[0], self.drivers[1], self.drivers[2], self.drivers[3]
        a = a.car.max_speed * randint(1, 10)


class Championship:
    def __init__(self, count_races):
        pass

    def __int__(self):
        pass

    def top_3(self):
        pass
