##file_name = input("Please enter a file name: ")
##
##all_lines=[word.strip() for line in open(file_name, "r")]
##two_v_words=[word for line in all_lines for word in line.split() \
##             if len([let for let in word if let in "aeiou"])>=2]
##
##print("The words in the file: ", all_lines)
##print("The words in the file that contain 2 or more vowels: ", two_v_words)
##
#-----------------------------------------------------------------------------
userPhrase = input("Please enter the phrase to translate: ")

dictTranslation = {"1":"i", "3":"e", "4":"a", "5":"s", "7":"t"}

print("Output: ", "".join([str(userPhrase.split(" ")) for char in userPhrase if dictTranslation.get(char) for char in userPhrase]))

"".join([
