import csv
import datetime
               
    
def listCharacters():
    with open("star-wars.csv") as file:
        data = list(csv.DictReader(file))
        print("-" * 70)
        print("MAIN CHARACTERS")
        print("Star Wars: Episode VII: The Force Awakens (2015)")
        print("-" * 70)

        for row in data:
            print(row["character"], " " * (30 - len(row["character"])) , row["name"], " " * (30 - len(row["name"])), row["birthday"])


listCharacters()


def getBios():
    with open("star-wars.csv") as file:
        data = list(csv.DictReader(file))
    print("-" * 70)
    print("BIOS")
    print("-" * 70)
    for row in data:
        row["birthday"] = row["birthday"].split("/")

        char = row["character"]
        name = row["name"]
        birth = row["birthday"]

        month = int(row["birthday"][0])
        day = int(row["birthday"][1])
        year = int(row["birthday"][2])

    
        birthday = datetime.date(year, month, day)
        now = datetime.date.today()
        age = (now - birthday)
        age = int(age.days // 365)
        
        print(char, "is played by", name + "\nwho was born on", \
              birthday.strftime("%A, %b %B, %Y.\n") + name , "is", age, "years old.\n")
#getBios()

def bornFriday():
    with open("star-wars.csv") as file:
        data = list(csv.DictReader(file))
    print("-" * 70)
    print("BIOS")
    print("-" * 70)

    birthdays = []
    for row in data:
        row["birthday"] = row["birthday"].split("/")
        char = row["character"]
        name = row["name"]
        birth = row["birthday"]

        month = int(row["birthday"][0])
        day = int(row["birthday"][1])
        year = int(row["birthday"][2])

        birthday = datetime.date(year, month, day)
        now = datetime.date.today()
        age = (now-birthday)
        agefloat = age.days / 365

        birthdays.append(birthday)

    for i in range(len(birthdays)):
        now = datetime.date.today()
        age = now - birthdays[i]
        years = age.days // 365

        if birthdays[i] == min(birthdays):
            print("The oldest cast member is: ", data[i]["name"], "who is", years, "years old." )
        if birthdays[i] == max(birthdays):
            print("The youngest cast member is: ", data[i]["name"], "who is", years, "years old." )

    print("\nCast members born on a Friday: ")
    for i in range(len(birthdays)):
        if birthdays[i].strftime("%A") == "Friday":
            print(data[i]["name"])

bornFriday()
                
