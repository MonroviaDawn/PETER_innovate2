# #list is square bracket - single values
# poke_1 = [
#     "Raiju", "Orange", "Excitebale"
# ]

# #dictionaries curly brackets - values with keys
# poke_2 = { 
#     "name":"Moedi", "color": "Purple", "mood": "Pessimist"
# }

# print(poke_1[0]) #!how ot call from a list
# print(poke_2["name"]) #! how to call from a dictionary

# name = poke_2["name"]

# print(f"My toughest advesary was {name}!")

# print("you can also conccatinate info also so " + poke_2["color"] + " would be the poke colour")

# #items in dictionaries can be updated in the usual way
# poke_2["mood"] = "perky"
# print(poke_2["mood"])

# #complex dictionary - like nested arrays in JS kinaa kinna - mindful of formatting, commas, spaces etc

# complex_dict = {
#     "one": { "name" : "Regent",
#         "age" : 51,
#         "team" : "Plymouth & Argyle"
#     },
#     "two": {"name": "Doug",
#         "age" : 15,
#         "team" : "Chelski"}
# }

# print(complex_dict["two"]["age"])

#ACTIVITY ONE ###################

# petionary = { "species" : {
#     "tiger": {
#         "size": "large",
#         "tempermeant" : "complex",
#         "apetite" : "relaxed",
#         "color": "orange",
#         "experience required" : "elite"
#         },
#     "pony" : {
#         "size": "large",
#         "tempermeant" : "docile",
#         "appetite" : "moderate",
#         "color": "brown",
#         "experience required" : "professional"
#         },
#     "Hamster" : {
#         "size": "tiny",
#         "tempermeant" : "very active",
#         "appetite" : "light",
#         "color": "gold",
#         "experience required" : "novice"
#     }
# }
# }

# print(petionary["Hamster"]["size"])
# print(petionary.keys())

###ACTIVITY2#########

countries = { "country" : {
    "Spain": {
        "capital": "Madrid"
        # "population" : "",
        # "work life balance" : "",
        # "weather rating": "A",
        },
    "France" : {
        "capital": "Paris"
        # "population" : "",
        # "work life balance" : "",
        # "weather": "",
        },
    "United Kingdom" : {
        "capital": "London"
        # "population" : "",
        # "work life balance" : "",
        # "weather": "",
        },
    "Italy" : {
        "capital": "Rome"
        # "population" : "",
        # "work life balance" : "",
        # "weather": "",
        },
    "Germany" : {
        "capital": "Berlin"
        # "population" : "",
        # "work life balance" : "",
        # "weather": "",
        },
}
}

#print(countries)
print(countries["country"]["Italy"]["capital"])
print(list(countries["country"]))

countries.setdefault("St. Kitts", True )


print(countries)

countries.setdefault("Mexico", True)
print(list(countries))

countries.setdefault("St. Kitts", "Basseterre")
print(countries["country"]["Germany"]["capital"])
print(countries["country"])