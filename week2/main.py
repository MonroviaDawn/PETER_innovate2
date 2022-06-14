from person import Person

ranger = Person("ranger", 44, "12'3", "capricorn", "squash") #the person "ranger" is declared and given attributes with data in the corresponding positions of the class set in the person.py file

studdart = Person("studdart", 38, "6'3'", "aries", "singing")
monty = Person("monty", 67, "6'1'", "libra", "scotch")
rosa = Person("rosa", 32, "5'6", "capricorn", "swimming")
brandy = Person("brandy", 25, "5'9", "aquarius", "math")


brandy.set_hair("long black braided")
brandy.get_hair()

# print(brandy.hair)