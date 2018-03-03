class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


<<<<<<< HEAD
class Flashlight(Item):
    def __init__(self, name, description, value):
        self.name = "Flashlight"
        self.description = "A rusty antique, emits a steady, glowing beam."
        self.value = 1

    def use(self):
        #Turn on flashlight, turn off flashlight, illuminate dark areas when turned on
        print("the flashlight flickers but does nothing as this feature is not implemented")

=======
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
>>>>>>> 7dab0dd6bc7bc1d2fdce9201978d964241e6daf2
