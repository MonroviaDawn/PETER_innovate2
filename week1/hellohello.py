# import random




# greeting = "hello world! im back and busy"
# print(greeting)
# print(len(greeting))
# print(greeting[1])
# greeting = greeting.replace("world", "busy")
# print(greeting)

# ACTIVITY 1

# string = "Welcome to Code Nation"

# stringlen = len(string)

# def find_even():
#     if stringlen%2 == 0:
#         print (f"{string} ! The length of {stringlen} makes this is an even string!")
#     else:
#         print (f"Ouch! Sorry but {stringlen} isnt quite what we're looking for :p")
#     string += random.randint(0,9)
# find_even()


# ACTIVIY 2

alphabet = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p", "q", "r", "s", "t", "u" ,"v", "w", "x", "y", "z" 
]

print(alphabet)

alphaindex = 0
def iterate_tool(list_selector):
    for i in alphabet:    
        username = input - 1
        print(alphabet[i])

def user_selection(list_selector):

        username = input("Tell me what you want...in numbers only!")
        username = int(input("now choose a number between 0-26 for your username"))
        print(f"Number {username} is {list_selector[input - 1]}")

    user_selection()



def find_username():
    username = input("please choose number between 1-26")
    username = int(usernum) - 1
    print(username)

find_username()




# print(int(5.4))
# print(int("54"))

# print("what is your name?")
# name = input()

# if name:
#     print(f"Hello {name}, how are you?")
# else:
#     print("you did not give me your name!")


# # lIST OF CARDS EX

# list_of_cards = ["jack", 
#     "queen", 
#     "king", 
#     "ace"
# ]

# if "ace" not in list_of_cards:
#     print("The ACE is missing")
# elif "2" not in list_of_cards and "3" not in list_of_cards:
#     print("no no no")

# if "ten" not in list_of_cards:
#     print("Ten is missing")
#     list_of_cards.append("Ten")


# TRY // EXCEPT 

def add_up():
    num1 = int(input("whats the firs number youd like to add up?"))
    num2 = int(input("whats the second numebr youd like to add up?"))

    try:
        print(f"{num1} + {num2} is {(int(num1) + (int(num2))}!")

    except:
        print("\n Error: please input numerical values. \n")
        print("**************")
add_up()