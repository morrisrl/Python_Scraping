##set_a = []
##def squares(i):
##    set_a = [i*i for i in range(0, i+1)]
##    return set_a
##
###main
##print(squares(10))

#-------------------------------------------------------------

##numbers = []
##userLower = int(input("Please enter a lower bound (int): "))
##userUpper = int(input("Please enter an upper bound (int): "))
##userDivide = int(input("Please enter a number to divide by (int): "))
##
##numbers = [num for num in range (userLower, userUpper+1) if num%userDivide == 0]
##print("All of the numbers between", userLower ,"and", userUpper, "that are divisible by",userDivide,":", numbers)

#--------------------------------------------------------------
vowels=["a", "e", "i", "o", "u"]
file_contents = [line.strip("\n") for line in open("words.txt", "r")]
print("All words in the file:", file_contents)

for word in file_contents:   
    if word.strip(vowels) in word:
        print("The words in the file that contain 2 or more vowels:", word)
        
