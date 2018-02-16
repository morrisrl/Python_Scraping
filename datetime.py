import os
home = os.getcwd()
os.path.isdir(home)

# Write an algorithm for a small program that looks through all objects in a given
# direvtory to find the total size in bytes of all files in that directory


# Import os
# def total_file(user_input)
# list all possible files, creates a new list
# Size = 0 (get size), grab file size 
# Check if the given directory is a file
# for item in user_directory:
#   if user_input is a file:
#       add file size to size (total) (+=)
#   elif user_input is a directory:
#       call our total_file() function
#       makes list of files
#       add file size to total count
#
# If something is a file,
#  Calculate 



##import os
##
##def total_file(user_input):
##    total = 0
##
##    for item in os.listdir(user_input):
##        if os.path.isfile(item):
##            total += os.path.getsize(item)
##        elif os.path.isdir(item):
##            new_file = os.path.join(os.getcwd(), item)
##            total += total_file(new_file)
##    return total 
##            
##            
##main
##user_input = input("Please enter a file.")
##total_file(user_input)
##print total_file 
    

import datetime
now = datetime.date.today()
birthday = datetime.date(1995, 10, 24)
age= now-birthday
print("I am", age.days, "days old.")
print("Which is", age.days/365, "years.")
      
##print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d of %B"))

import random
import datetime
import time

start=time.clock()
random.randrange() 

for i in random.randrange(1900, 2001):
    print(i)
end=time.clock()
print(now.strftime("%m-%d-%y. %d %b %Y is a
%A on the %d day of %B"))
