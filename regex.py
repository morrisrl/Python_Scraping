#1) The Python regular expression pattern that would match a hex color code is
#   [a-f0-9]{6}|[a-f0-9]{3}


#2) Import re, urllib.request, sll (for Macs)
#   Create a function for our URL
#   Read in the webpage
#   Create a variable for wins that will look for all of the wins on the webpage
#      (When we examine the HTML code, we see that wins are denoted by the div tag,
#       a capital "W" and the corresponding score, so we want to make sure we grab the
#       scores between the two div tags to make sure we are grabbing the score and nothing else.
#       This will be the same for losses except we grab the div tag and "L" for losses.
#   Create a variable for losses that will look for all of the losses on the webpage.
#   Since we want the amount of wins/losses, we need to print of the number of times the win and loss scores show up
#   We do this by printing the length of each list

#3)

import re, urllib.request, ssl

def scores(url):
    context = ssl._create_unverified_context()
    web_page = urllib.request.urlopen(url, context=context)
    lines = web_page.read().decode(errors="replace")

    wins = re.findall('(?<=<div>W).+?(?=</div>)', lines)
    losses = re.findall('(?<=<div>L).+?(?=</div>)', lines)

        
    
    print("Wins:",len(wins))
    print("Losses:",len(losses))
##  print("Total Difference:",
        

scores("http://cgi.soic.indiana.edu/~dpierz/mbball.html")
