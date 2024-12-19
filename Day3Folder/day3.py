# name = input("what is your name?")
# ask = input("how are you?")
# print (name + " is" +  ask + " today")

# num1 = int(input("give a random odd num "))
# num2 = int(input("give a ramdom even num 9"))
# print ( str (num1) + "+" + str (num2) + "=" + str (num1 + num2) )

# gm = int(input("How old is your grandmather? "))
# gf = int(input("How old is your grandfather? "))
# if gm > gf:
#     print("Your grandmother is older than your grandfather.")
# else:
#     print("Your grandfather is older than your grandmother.")

# corr_pas = 6969
# pas = int(input("What is the password?"))
# if corr_pas == pas:
# print("The door is opened")
# else:
# print("WRONG PASSWORD. SKILL ISSUE!!!")

# password = "p@ssword"
# person_password = "unknown"
# tries = 0

# for i in range(3):
#     if person_password != password:
#         person_password = input("what is the password?")
#         if tries < 3:
#             if person_password == password:
#                 print ("you have logged in")
#             else:
#                 print ("WRONG PASSWORD !!! try again")
#                 tries = tries + 1
# if tries >= 3:
#     print("SKILL ISSUE!!!")

import random 

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
ans = num1+ num2

per_ans = num1 + num2

per_ans =int(input("what is " + str(num1) + "+" + str(num2) + "?"))