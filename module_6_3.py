from random import randint

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0]

    def __init__(self, speed):
        self.speed = speed

    def move(self, dx, dy, dz):
        if dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [dx * self.speed, dy * self.speed, dz * self.speed]

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        eggs = randint(1,4)
        if eggs == 1:
            print(f'Here is {eggs} egg for you')
        else:
            print(f'Here are {eggs} eggs for you')

class AquaticAnimal(Animal):

    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self.speed /= 2
        dz_new = int(abs(self._cords[2] - dz * self.speed))
        self._cords[2] = dz_new

class PoisonousAnimal(Animal):

    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):

    sound = '"Click-click-click'
    _DEGREE_OF_DANGER = PoisonousAnimal._DEGREE_OF_DANGER




db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
