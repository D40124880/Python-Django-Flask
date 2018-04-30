# #import the library
# import urllib
# # NOTE: there's a urllib version for each version of Python:
# # Use urllib2 if you're using Python 2
# # Use urllib3 for Python 3
# # Finally, use it...
# # urllib.urlopen(...context)

# >>>import urllib
# >>>dir(urllib)
# ['ContentTooShortError', 'FancyURLopener', 'MAXFTPCACHE', 'URLopener', '__all__', '__builtins__', '__doc__', 
# '__file__', '__name__', '__package__', '__version__', '_asciire', '_ftperrors', '_get_proxies', '_get_proxy_settings', 
# '_have_ssl', '_hexdig', '_hextochr', '_hostprog', '_is_unicode', '_localhost', '_noheaders', '_nportprog', 
# '_passwdprog', '_portprog', '_queryprog', '_safe_map', '_safe_quoters', '_tagprog', '_thishost', '_typeprog', 
# '_urlopener', '_userprog', '_valueprog', 'addbase', 'addclosehook', 'addinfo', 'addinfourl', 'always_safe', 'base64', 
# 'basejoin', 'c', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 'getproxies_environment', 'getproxies_macosx_sysconf', 
# 'i', 'localhost', 'noheaders', 'os', 'pathname2url', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_macosx_sysconf', 
# 'quote', 'quote_plus', 're', 'reporthook', 'socket', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 
# 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'test1', 'thishost', 'time', 
# 'toBytes', 'unquote', 'unquote_plus', 'unwrap', 'url2pathname', 'urlcleanup', 'urlencode', 'urlopen', 'urlretrieve']
# >>>help(urllib)

# from my_package.subdirectory import my_functions

# import my_modules.test_module
# OR
# import my_modules import test_module

# __init__.py
# __all__ = ["test_module"]

# sample_project
#      |_____ python_file.py
#      |_____ my_modules
#                |_____ __init__.py
#                |_____ test_module.py
#                |_____ another_module.py
#                |_____ third_module.py

# # instantiate class User
# class User(object):
#     # this method to run every time a new object is instantiated
#     def __init__(self, name, email):
# 	# instance attributes 
#         self.name = name
#         self.email = email
#         self.logged = True
#     # login method changes the logged status for a single instance (the instance calling the method)
#     def login(self):
#         self.logged = True
#         print self.name + " is logged in."
#         return self
#     # logout method changes the logged status for a single instance (the instance calling the method)
#     def logout(self):
#         self.logged = False
#         print self.name + " is not logged in"
#         return self
#     # print name and email of the calling instance
#     def show(self):
#         print "My name is {}. You can email me at {}".format(self.name, self.email)
#         return self

# --------------------------------------------------------------------------------------------------------------

class Vehicle(object):
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0
    def drive(self,miles):
        self.mileage += miles
        return self
    def reverse(self,miles):
        self.mileage -= miles
        return self
class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"
class Car(Vehicle):
    def set_wheels(self):
        self.wheels = 4
        return self
class Airplane(Vehicle):
    def fly(self, miles):
        self.mileage += miles
        return self
v = Vehicle(4,8,"dodge","minivan")
print v.make
b = Bike(2,1,"Schwinn","Paramount")
print b.vehicle_type()
c = Car(8,5,"Toyota", "Matrix")
c.set_wheels()
print c.wheels
a = Airplane(22,853,"Airbus","A380")
a.fly(580)
print a.mileage

# class Parent(object): # inherits from the object class
#   # parent methods and attributes here
# class Child(Parent): #inherits from Parent class so we define Parent as the first parameter
#   # parent methods and attributes are implicitly inherited
#   # child methods and attributes

#put a ----- * ------- to receive many inputs at once
def varargs(arg1, *args):
  print "Got "+arg1+" and "+ ", ".join(args)
varargs("one") # output: "Got one and "
varargs("one", "two") # output: "Got one and two"
varargs("one", "two", "three") # output: "Got one and two, three"


def varargs(arg1, *args):
   print "args is of " + str(type(args))
varargs("one", "two", "three") # output: args is of <type 'tuple'>


from human import Human
class Wizard(Human):
    def __init__(self):
        super(Wizard, self).__init__()   # use super to call the Human __init__ method
        self.intelligence = 10           # every wizard starts off with 10 intelligence
    def heal(self):
        self.health += 10
class Ninja(Human):
    def __init__(self):
        super(Ninja, self).__init__()    # use super to call the Human __init__ method
        self.stealth = 10                # every Ninja starts off with 10 stealth
    def steal(self):
        self.stealth += 5
class Samurai(Human):
    def __init__(self):
        super(Samurai, self).__init__()  # use super to call the Human __init__ method
        self.strength = 10               # every Samurai starts off with 10 strength
    def sacrifice(self):
        self.health -= 5
