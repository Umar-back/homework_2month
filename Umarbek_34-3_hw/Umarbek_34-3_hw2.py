class SuperHero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.fly = False

    def double_health(self):
        self.health **= 2
        self.fly = True

    def true_in_true_phrase(self):
        return f"True in the {self.__class__.__name__}_phrase"

class AirHero(SuperHero):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage

class EarthHero(SuperHero):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage

class SpaceHero(SuperHero):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage

class Villain(SuperHero):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage
        self.people = "monster"

    def gen_x(self):
        pass

    def crit(self, target):
        if isinstance(target, SuperHero):
            target.health -= self.damage


air_hero = AirHero("AirMan", 50, 10)
earth_hero = EarthHero("EarthMan", 50, 10)
space_hero = SpaceHero("SpaceMan", 100, 30)
villain = Villain("EvilVillain", 200, 50)

air_hero.double_health()
earth_hero.double_health()
space_hero.double_health()
print(air_hero.true_in_true_phrase())
print(earth_hero.true_in_true_phrase())
print(space_hero.true_in_true_phrase())

villain.crit(air_hero)

print(f"{air_hero.name} health after attack: {air_hero.health}")
