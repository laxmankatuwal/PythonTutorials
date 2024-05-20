import random
import string

# target = random.randint(1,100)

# while True:
#     userChoice = input("Guess the number or Quit:")
#     if(userChoice == "Quit"):
#         break
#     userChoice = int(userChoice)
#     if(userChoice == target):
#         print("Success! : Correct Guess!!")
#         break

#     elif(userChoice < target):
#         print("Your choice is to small, Guess larger ")

#     else:
#         print("Your choice is to big , Guess smaller one")


# print("_____Game Over_____")


#RANDOM PASSWORD GENERATOR PROJECT

pass_len = 8
char_val = string.ascii_letters + string.digits + string.punctuation
# password = "".join([random.choice(char_val) for i in range(pass_len)])

#next method simple method

password = ""
for i in range(pass_len):
    password += random.choice(char_val)

print("Your password is:", password)
