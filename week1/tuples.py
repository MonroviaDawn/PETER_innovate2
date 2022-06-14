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

# alphabet = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p", "q", "r", "s", "t", "u" ,"v", "w", "x", "y", "z" 
# ]

# print(alphabet)

# alphaindex = 0
# def iterate_tool(list_selector):
#     for i in alphabet:    
#         username = input - 1
#         print(alphabet[i])

# def user_selection(list_selector):

#         username = input("Tell me what you want...in numbers only!")
#         username = int(input("now choose a number between 0-26 for your username"))
#         print(f"Number {username} is {list_selector[input - 1]}")

#     user_selection()



# def find_username():
#     username = input("please choose number between 1-26")
#     username = int(usernum) - 1
#     print(username)

# find_username()




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

# def add_up():
#     num1 = int(input("whats the firs number youd like to add up?"))
#     num2 = int(input("whats the second numebr youd like to add up?"))

#     try:
#         print(f"{num1} + {num2} is {(int(num1) + (int(num2))}!")

#     except:
#         print("\n Error: please input numerical values. \n")
#         print("**************")
# add_up()



# TRY // EXCEPT 

# def add_up():
#     num1 = int(input("whats the firs number youd like to add up?"))
#     num2 = int(input("whats the second numebr youd like to add up?"))

#     try:
#         print(f"{num1} + {num2} is {(int(num1) + (int(num2))}!")

#     except:
#         print("\n Error: please input numerical values. \n")
#         print("**************")
# add_up()

# SCOPE

# light = False
# def light_switch():
#     global light
#     if light:
#         print("Seems a little light out")
#         light = False
#     else:
#         print("wheres the light gone?")
#         light = True

# light_switch()
# light_switch()





# even_nums = [2,4,6,8,10] #!mutuable
# odd_nums = (1,3,5,7,9) #!immutubale

# alphabet = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p", "q", "r", "s", "t", "u" ,"v", "w", "x", "y", "z" 
# ]

# print(alphabet)

# alphaindex = 0
# def iterate_tool(list_selector):
#     for i in alphabet:    
#         username = input - 1
#         print(alphabet[i])

# def user_selection(list_selector):
    
#         username = input("Tell me what you want...in numbers only!")
#         username = int(input("now choose a number between 0-26 for your username"))
#         print(f"Number {username} is {list_selector[input - 1]}")

#     user_selection()



# def find_username():
#     username = input("please choose number between 1-26")
#     username = int(usernum) - 1
#     print(username)

#     return alp

# find_username()


# #SLICE more in depth way of maniuplating lists#

# my_list = [
#     1, 2, 3, 4, 5, 6, 7, 8, 9
# ]

# print(my_list[2]) #counts from start

# print(my_list[-2]) #counts from end

# print(my_list[4:-2]) #colon would indicate a range betwen first index mentioned to last sp in this case 4th position to 2md position from the end.

# print(my_list[4:-2:2]) #an extra parameter indicated the size of the steps between so in this case steps of 2



# ACTIVITY 1


def chooser():
    key = input("please enter a number.")
    try:
        key = int(key)
        if key % 1 == 0:
            print(f"{key}? good choice")
    except:
            print("oops try again!")
            chooser()

chooser()