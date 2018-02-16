##user_input = ""
##total = 0
##
##while user_input != "STOP":
##    user_input = input("Please enter a number or STOP ")
##    total += int(user_input)
##    print(user_input)
##    if user_input == "STOP":
##        print("STOP")
##        print("The total sum is", total)
##        break 
##    

# -----------------------------------------------------------------------------

#Use elif to write a program that takes 10 numbers from the user and sorts them
    #into 3 lists

#Declare 3 blank lists, one for odds, evens, and other
#Get 10 numbers from the user and sort them into the lists

#   Take each number

#   Is it even?
#       Put 

##evenList = []
##oddList = []
##otherList = []
##
##for i in range(10):
##    userInput = eval(input("Please enter a number: "))
##    if userInput%2 == 0:
##        evenList.append(userInput)
##    elif userInput%2 == 1:
##        oddList.append(userInput)
##    else:
##        otherList.append(userInput)
##
##print("Evens: ", evenList)
##print("Odds: ", oddList)
##print("Others: ", otherList)

#   ---------------------------------------------------------
#  DICTIONARIES

scores = {"Dave": 125, "Abby": 100, "Carrie": 275, "Ben": 150}

names = sorted(scores.keys())

print("Current Players: ")
for name in scores:
    print(name, end =" ")
user_in = input("Please enter a player name: ")
if user_in in scores:
    print("The score for", user_in, scores.get(user_in))
else:
    print("The score for ", user_in, "is not found.")

