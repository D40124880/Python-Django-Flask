name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "blah blah blah"]

def make_dict(list1, list2):
    if (len(list1) > len(list2)):
        new_dict = {key:value for key, value in zip(list1, list2)}
    elif (len(list1) < len(list2)):
        # new_dict = {key:value for key, value in zip(list2, list1)}
        dictionary = dict(zip(list2, list1))
        return dictionary
    else:
        new_dict = {key:value for key, value in zip(list1, list2)}
    return new_dict

print make_dict(name, favorite_animal)