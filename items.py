class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)


class Flashlight(Item):
    def __init__(self):
        super().__init__(
            name = "Flashlight",
            description = "A rusty antique, emits a steady, glowing beam.",
            value = 1
        )
    def use(self):
        #Turn on flashlight, turn off flashlight, illuminate dark areas when turned on
        print("the flashlight flickers but does nothing as this feature is not implemented")

=class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)



class Stick(Weapon):
    def __init__ (self):
        super().__init__(
            self.name = "Stick"
            self.description = "A small, swishy stick. Good for poking things."
            self.value = 1
            self.damage = 1)

    def use(self):
        #Poke with stick, throw stick, drop stick, burn stick
        print ("The stick pokes! It causes dubious damage!")

class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5)

class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10)