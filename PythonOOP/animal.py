class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health = self.health - 1
        return self
    def run(self):
        self.health = self.health - 5
        return self
    def display_health(self):
        print "Animal's health:", self.health
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)

    def pet(self):
        self.health = self.health + 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)
    def fly(self):
        self.health = self.health - 10
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am  dragon"

animal1 = Animal("Tiger", 34)

animal2 = Dog("Golden Retriever")

animal3 = Animal("cheetah", 578)

animal1.walk().walk().walk().run().run().display_health()

animal2.walk().walk().walk().run().run().display_health()

animal3.display_health()