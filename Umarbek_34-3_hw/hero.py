class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def health(self):
        self.health_points *= 2

    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health Points: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero("Piter Parker", "Spiderman", "Run and Super Strength", 50, "Piter Parker ne LOX!")
print(hero.get_name())
hero.health()
print(hero)
print(len(hero.catchphrase))