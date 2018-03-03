import random

class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

    def speak(self):
        print("Grrrrrr")


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=2)

    #def:

class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15)


# Goblinoids

class Goblinoid(Enemy):

    def speak(self):
        action = ["stomp", "bite", "break", "munch", "kick", "headbutt", "tickle"
                  "reorganize", "steal", "softly caress", "punch holes in", "tear off"]
        bodypart = ["legsticks", "thighbones", "earlobes", "eyeballs", "face", "butt",
                    "cheeks", "belly", "tongue", "toes", "hair", "bone-jelly"]

        a = random.choice(list(action))
        b = random.choice(list(bodypart))

        print("I'm gonna {0} your {1}!".format(a,b))

class Goblin(Goblinoid):
    def __init__(self):
        super().__init__(name="Goblin", hp=10, damage=3)

class LargeGoblin(Goblinoid):
    def __init__(self):
        super().__init__(name="Large Goblin", hp=14, damage=4)

class FatGoblin(Goblinoid):
    def __init__(self):
        super().__init__(name="Fat Goblin", hp=24, damage=2)


