class Panda:

    def __init__(self, name, age, weight):
        self._name = name
        self._age = age
        self._weight = weight

    def eat(self, amount):
        self._weight += amount

    def sleep(self):
        self._age += 1

    def get_age(self):
        return self._age

    def _get_weight(self):
        pass

ivo = Panda('Ivo', 22, 80)
ivo.sleep()
ivo.eat(2)
ivo._age = 1
print(ivo._age, ivo.weight)
print(ivo._get_age)
