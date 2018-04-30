class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"
    def sell(self):
        self.status = "Sold"
        return self
    def add_tax(self):
        tax = self.price * 0.06
        self.price = self.price + tax
        return self
    def returning(self, status):
        if status == "defective":
            self.status = "defective"
            self.price = 0
        elif status == "returned in box":
            self.status = "For Sale"
        elif status == "opened":
            self.status = "used"
            tax = self.price * 0.2
            self.price = self.price - tax
        return self
    def display_info(self):
        print "Price: ${}" .format(self.price)
        print "Item Name: ", self.item_name
        print "Weight: ", self.weight
        print "Brand: ", self.brand
        print "Status: ", self.status
        return self

item1 = Product(234, "Camera", 23, "Canon")

item1.returning("opened").add_tax().display_info()