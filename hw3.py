#Rachel Morris | HW 4 | Group 5

#   1) You can find the Standard Documentation for Python by going to Python.org and clicking on 
#      "Documentation" in the navigation menu where you can find the Python Standard Library.
#--------------------------------------------------------------
#2) ALGORITHM

#   import os
#   import datetime (for bonus)
#   create a function that will allow us to go through and rename files
#   ask for user input to a directory
#   go/change into that user's directory
#   iterate through that user's directory, going through the list of files
#      check if it is a file:
#         when "draft" is found in file, replace it with "final"
#         append this to our new file so the user file will now be the new file with "draft" removed and "final" in its place

# BONUS:
#         open new file in append mode to be able to add new data to the file
#         (taken from http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python)
#	      write on that file our date/time using our datetime module
#	      close the file
#    call the function
#-------------------------------------------------------------
#3) 

import os
import datetime #for bonus

def renameFile():
    userPath = input("Please enter a path to a directory.")
    os.chdir(userPath)
    for userFile in os.listdir(os.getcwd()):
        if os.path.isfile(userFile):
            newFile = userFile.replace("draft", "final")
            #os.rename(userFile, newFile) not sure if this part is entirely necessary since I'm already using replace
        print(os.getcwd)
#BONUS  
            fileOpen = open(newFile, "a")
            fileOpen.write("Edited on" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            fileOpen.close()

#main
renameFile()
