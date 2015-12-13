import unittest
from championship import Car
from championship import Driver
from championship import Race


class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = 'Opel'
        self.model = 'Astra'
        self.max_speed = 180
        self.test_car = Car(self.car, self.model, self.max_speed)

    def test_car_str(self):
        self.assertEquals(str(self.test_car),
                          "{} {} with max speed of: {}".format(self.car, self.model, self.max_speed))

    def test_car_int(self):
        self.assertEquals(int(self.test_car), self.max_speed)


class TestDriver(unittest.TestCase):

    def setUp(self):
        self.name = 'Ivo'
        self.car = 'Opel'
        self.model = 'Astra'
        self.max_speed = 180
        self.test_car = Car(self.car, self.model, self.max_speed)
        self.test_driver = Driver(self.name, self.test_car)

    def test_driver_str(self):
        self.assertEquals(str(self.test_driver),
                          "{} drives {} {}".format(self.name, self.test_car.car, self.test_car.model))


class TestRace(unittest.TestCase):

    def setUp(self):
        self.name = 'Ivo'
        self.car = 'Opel'
        self.model = 'Astra'
        self.max_speed = 180
        self.test_car = Car(self.car, self.model, self.max_speed)
        self.test_driver = Driver(self.name, self.test_car)
        self.test_race = Race([self.test_driver], 0.7)

    def test_init(self):
        self.assertEquals(self.test_race.drivers, [self.test_driver])


if __name__ == '__main__':
    unittest.main()
