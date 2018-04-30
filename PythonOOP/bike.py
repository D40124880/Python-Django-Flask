class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
        miles = 0
    def displayInfo(self):
        print "Bike's price is at: ${}" .format(self.price)
        print "Bike speed is at: ", self.max_speed, "mph"
        print "Bike's miles at: ", self.miles
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        if(self.miles < 0):
            self.miles = 0
        return self

new_bike1 = Bike(278, 60, 34)
new_bike2 = Bike(243, 34, 2)
new_bike3 = Bike(342, 233, 10)

new_bike1.ride().ride().ride().reverse().displayInfo()
new_bike2.ride().ride().reverse().reverse().displayInfo()
print #for spacing
new_bike3.reverse().reverse().reverse().displayInfo()