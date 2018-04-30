context = {
  'questions': [
   { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
   { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
   { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
   { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
  ]
 }

for key, data in context.items():
    #print data
    for value in data:
        print "Questions #", value['id', ": ", value ['content']]
        print "----"

    # the result is ----
    # Question # 1 :  Why is there a light in the fridge and not in the freezer?
    # ----
    # Question # 2 :  Why don't sheep shrink when it rains?
    # ----
    # Question # 3 :  Why are they called apartments when they are all stuck together?
    # ----
    # Question # 4 :  Why do cars drive on the parkway and park on the driveway?
    # ----

data = {"House": "Huas", "cat": "katze", "red":"rot"}

print data.items()
#[('house', 'Haus'), ('red', 'rot'), ('cat', 'Katze')]

print data.keys()
#['house', 'red', 'cat']

print data.values()
#['Haus', 'rot', 'Katze']

#combining dictionaries with zip()
countries = ["Italy", "Germany", "Spain", "USA", "Switzerland"]
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]

country_specialities_dict = zip(countries, dishes)
print country_specialities_dict

#to print all keys
for data in capitals:
     print data
#another way to print all keys
for key in capitals.iterkeys():
     print key
#to print the values
for val in capitals.itervalues():
     print val
#to print all keys and values
for key,data in capitals.iteritems():
     print key, " = ", data
