class Animal:
    live = True
    sound = None # звук изначально отсутствует
    _DEGREE_OF_DANGER = 0 # Степень опасности существа
    def __init__(self, _cords = [0, 0, 0], speed = 0):
        self._cords = _cords
        self.speed = speed

    def move(self, dx, dy, dz):
        self.dx = dx
        self.dy = dy
        self.dz = dz
        x = self._cords[0] + dx * self.speed
        y = self._cords[1] + dy * self.speed
        z = self._cords[2] + dz * self.speed

        if z < 0:
            print("It's too geep, i can't dive :(") # это слишком круто, я не могу нырять
        else:
            self._cords = [x, y, z]

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I'm peaceful :)") # извините, я миролюбивый
        else:
            print("Be careful, I'm attacking you 0_0")

    def speak(self):
        if self.sound != None:
            print(self.sound)


from random import randint

class Bird(Animal):
    beak = True # наличие клюва

    def lay_eggs(self):
        print(f"Here are(is) {randint(1, 4)} eggs for you") # вот яйца для тебя

class AguaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self.dz = dz
        z = abs(self.dz) * self.speed / 2
        self._cords[2] -= z

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, AguaticAnimal, Bird):
    sound = 'Click-click-click'

    def __init__(self, speed):
        self.speed = speed
        super().__init__()
        self.speed = speed

db = Duckbill(10)

print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(3, 5, -1)
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()

