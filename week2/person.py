

# class Person():
#     def __init__(self) -> None:
#         self.name = None


# class Person():
#     def __init__(self, attribute_name): #definte attributes by adding names into the brackets while defining class
#         self.name = attribute_name    


class Person():
    def __init__(self, person_name, person_age, person_height, person_starsign,): #person_hobbies not needed as its being initiated as an empty list
        self.name = person_name
        self.age = person_age
        self.height = person_height
        self.starsign = person_starsign
        self.hobbies = []
    
    def set_hair(self, person_hair):
        self.hair = person_hair

    def get_hair(self):
        print(self.hair)

    def set_hobbies(self, person_hobbies):
        self.hobbies.append(person_hobbies)

    
