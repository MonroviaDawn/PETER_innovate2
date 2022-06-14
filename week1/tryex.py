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

light = False
def light_switch():
    global light
    if light:
        print("Seems a little light out")
        light = False
    else:
        print("wheres the light gone?")
        light = True

light_switch()
light_switch()


