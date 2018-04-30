class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0
    def info(self):
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

        if self.fuel > 40:
            self.fuel = "impossible! it does not have that much fuel!"
        elif self.fuel > 30:
            self.fuel = "Full"
        elif self.fuel > 10:
            self.fuel = "Kind Of Full"
        elif self.fuel >= 0:
            self.fuel = "Empty"
        else:
            self.fuel = "Negative numbers are unacceptable!"
        return self
    def display_all(self):
        print "Price: ${}" .format(self.price)
        print "Speed: {}mph" .format(self.speed)
        print "Fuel: ", self.fuel
        print "Mileage: {}mpg" .format(self.mileage)
        print "Tax: ", self.tax
        return self

car1 = Car(1232, 32, 40, 45)
car2 = Car(12341, 34, 23, 43)
car3 = Car(24524, 23, 5, 21)
car4 = Car(45635, 54, 6, 42)
car5 = Car(23445, 23, 12, 56)
car6 = Car(2344, 67, 45, 12)

car1.info().display_all()
print
car2.info().display_all()
print
car3.info().display_all()
print
car4.info().display_all()
print
car5.info().display_all()
print
car6.info().display_all()