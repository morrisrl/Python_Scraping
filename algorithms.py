# Rachel Morris | HW01 | 17 January 2018
# morrisrl
# Team 5 (I think?)

#2) Write an algorithm for a Rock Paper Scissors game

#  Import random (so that the computer can randomly choose)

#  Let computer randomly choose between rock, paper or scissors by putting options into a list
#  Get user input by asking user to enter rock, paper or scissors

#  If the computer's guess is rock, and the user's is paper:
#       Print a message that the user won with paper

#  Otherwise if computer's guess is rock, and the user's is scissors:
#       Print a message that the computer won with rock

#  Otherwise if computer's guess is paper, and the user's is scissors:
#       Print a message that the user won with scissors

#  Otherwise if computer's guess is paper, and the user's is rock:
#       Print a message that the computer won with paper

#  Otherwise if computer's guess is scissors, and the user's is paper:
#       Print a message that the computer won with scissors

#  Otherwise if computer's guess is scissors, and the user's is rock:
#       Print a message that the user won with rock

#  Else if the guesses are the same (otherwise none of the above situations occur):
#       Print a message that there was a tie.


#----------------------------------------------------
#3) Program that asks the user for string as input
#   and prints out a reversed order of that string

# Ask the user for a string
# Don't know what the new reverse string is, so make it an empty string for now
# Implement a for loop that looks through the user's input and iterate through that string
# Convert user string to length since we use range
# Reverse string will be the original user string that takes its length -1 - index position 
# Print the user string in reverse


userString = input("Please enter a string. ") 
reverseString = "" 

for i in range(len(userString)):
    reverseString += userString[len(userString)-1-i]
print(reverseString) 


#----------------------------------------------------
#4) Program that takes two lists and displays True if
#   at least one member in common, False otherwise

#   Make a function that looks for common items in two lists
#   Look through items in first list
#   Within that loop, look through items in other list
#   If item found in list One is found in list Two, return True
#   Otherwise no common items are found, so return False


listOne = ["peony", "orchid", "rose", "fern", "freesia"]
listTwo = ["daffodil", "larkspur", "hydrangea", "aster", "orchid"]

def commonItems(listOne, listTwo):
    for item in listOne:
        for sameItem in listTwo:
            if item == sameItem:
                return True
    return False

print(commonItems(listOne, listTwo))
