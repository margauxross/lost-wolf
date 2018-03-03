class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Flashlight(Item):
    def __init__(self, name, description, value):
        self.name = "Flashlight"
        self.description = "A rusty antique, emits a steady, glowing beam."
        self.value = 1

    def use(self):
        #Turn on flashlight, turn off flashlight, illuminate dark areas when turned on
        print("the flashlight flickers but does nothing as this feature is not implemented")

