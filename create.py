#presidents.py
#This program’s purpose is to provide the user requested information about the US Presidents

#Init
import time
import webbrowser
import pandas as pd
data = pd.read_csv("presidents.csv")
id = data['id'].tolist()
presidency = data['Presidency'].tolist() #Stores the PRESIDENTS' NUMERICAL DESIGNATION
president = data['President'].tolist() #Stores the names of EACH PRESIDENT
took_office = data['Took office'].tolist() #Stores when each president TOOK OFFICE
left_office = data['Left office'].tolist() #Stores when each president LEFT OFFICE
party = data['Party'].tolist() #Stores WHICH PARTY each president belongs to
portrait = data['Portrait'].tolist() #Stores each PRESIDENTIAL PORTRAIT
home_state = data['Home state'].tolist() #Stores each PRESIDENTS' HOME STATE
filter = [] #Used to FILTER DATA

#Functions
def presidents_number(): #Gives information on the president of a number
    pn = input("Which number are you searching for? ")
    for i in range(len(presidency)):
        if int(pn) == presidency[i]:
            filter.append(president[i])
    if len(filter) < 1:
        print("Input not recognized, please try again.")
    else:
        print(filter)
    filter.clear()

def numbers_president(): #Gives information on the president's number
    np = input("Which president are you searching for? (Full Name) ")
    for i in range(len(president)):
        if np.lower() == president[i].lower():
            filter.append(presidency[i])
    if len(filter) == 1 or len(filter) == 2:
        print(filter)
    else:
        print("President not recognized, please try again.")
    filter.clear()

def incumbent(): #Gives information on the incumbent president
    for i in range(len(left_office)):
        if 2026 == left_office[i]:
            print(f"""\033[1mPresident:\033[0m {president[i]} \033[1mPresidency:\033[0m {presidency[i]} \033[1mStarted term:\033[0m {took_office[i]}
\033[1mParty:\033[0m {party[i]} \033[1mHome State:\033[0m {home_state[i]}""")

def presidents_party(parti): #Gives information on the party of a president
    for i in range(len(party)):
        if parti.lower() == president[i].lower():
            filter.append(party[i])
    print(f"{parti.title()}'s party: {filter[0].title()}")
    filter.clear()

def parties_president(partie): #Gives information of all presidents from a party
    if partie.lower() == "independent":
        for i in range(len(party)):
            if party[i].lower() == "independent":
                filter.append(president[i])
    elif partie.lower() == "federalist":
        for i in range(len(party)):
            if party[i].lower() == "federalist":
                filter.append(president[i])
    elif partie.lower() == "democratic-republican":
        for i in range(len(party)):
            if party[i].lower() == "democratic-republican":
                filter.append(president[i])
    elif partie.lower() == "democratic":
        for i in range(len(party)):
            if party[i].lower() == "democratic":
                filter.append(president[i])
    elif partie.lower() == "whig":
        for i in range(len(party)):
            if party[i].lower() == "whig":
                filter.append(president[i])
    elif partie.lower() == "republican":
        for i in range(len(party)):
            if party[i].lower() == "republican":
                filter.append(president[i])
    if len(filter) > 0:
        print(f"{partie.title()} Presidents: {filter}")
    else:
        print("Party not recognized, please try again.")
    filter.clear()

def president_year(year): #Finds the president(s) that were in office during a year
    for i in range(len(took_office)):
        try:
            if int(year) >= took_office[i] and int(year) <= left_office[i]:
                filter.append(president[i])
        except:
            time.sleep(0)
    if len(filter) > 0:
        print(f"President during {year}: {filter}")
    elif len(filter) < 1:
        print(f"There is no president during {year}, please try again.")

def picture(): #Shows the presidential portrait of a president
    pic = input("Which presidential portrait would you like to view? (Full Name) ")
    for i in range(len(president)):
        if pic.lower() == president[i].lower():
            filter.append(portrait[i])
    if len(filter) == 1:
        webbrowser.open(filter[0])
    elif len(filter) == 2:
        photo = input("Term 1 or Term 2? ")
        if photo.lower() == "term 1":
            webbrowser.open(filter[0])
        elif photo.lower() == "1":
            webbrowser.open(filter[0])
        elif photo.lower() == "term 2":
            webbrowser.open(filter[1])
        elif photo.lower() == "2":
            webbrowser.open(filter[1])
        else:
            print("Input not recognized, please try again.")
        filter.clear()
    else:
        print("Input not recognized, please try again.")

def homestate(): #Gives information on presidents and their home states
    hs = input("""Do you want to know where a \033[1m[PRESIDENT]\033[0m is from
 or all presidents from a \033[1m[STATE]\033[0m? """)
    if hs.lower() == "president": #Finds where a president is from
        who = input("Which president? (Full Name) ")
        for i in range(len(president)):
            if who.lower() == president[i].lower():
                filter.append(home_state[i])
        if len(filter) == 1:
            print(f"{who} is from {filter[0]}")
        elif len(filter) == 2:
            print(f"{who} is from {filter[0]}")
        else:
            print("Name not recognized, please try again.")
    elif hs.lower() == "state": #Finds all the presidents from a state if applicable
        where = input("Which state? ")
        for i in range(len(president)):
            if where.lower() == home_state[i].lower() and president[i] not in filter:
                filter.append(president[i])
        if len(filter) == 0:
            print(f"There are no presidents from {where}, please try again.")
        else:
             print(f"Presidents from {where}: {filter}")
    else:
        print("Input not recognized, please try again.")

#Main
print("")
print("| Welcome to Presidents 101! |")
print("")
print("------------------------------")
while True:
    print("")
    time.sleep(0.5)
    stay = input("| Access presidential database? \033[1m[Y/N]\033[0m | ")
    if stay.lower() == "n":
        print("Hope you enjoyed!")
        break
    elif stay.lower() == "y":
        time.sleep(0.5)
        print("")
        q1 = input("""Would you like to see information about
\033[1m[NUMERICAL DESIGNATION]\033[0m \033[1m[INCUMBENT]\033[0m \033[1m[PARTY]\033[0m \033[1m[TERM]\033[0m \033[1m[PICTURE]\033[0m or \033[1m[HOME STATE]\033[0m?

-""")
        if q1.lower() == "numerical designation":
            q2 = input("""Are you searching for a president's number or a number's president?
\033[1m[1]\033[0m \033[1m[2]\033[0m """)
            if q2.lower() == "1":
                try:
                    presidents_number()
                except:
                    print("Input not recognized, please try again.")
                filter.clear()
            elif q2.lower() == "2":
                numbers_president()
                filter.clear()
            else:
                print("Input not recognized, please try again.")
        elif q1.lower() == "incumbent":
            incumbent()
            filter.clear()
        elif q1.lower() == "party":
            q3 = input("""Are you searching for a president's party or a party's presidents?
\033[1m[1]\033[0m \033[1m[2]\033[0m """)
            if q3.lower() == "1":
                partie = input("Which president are you searching for? (Full Name) ")
                try:
                    presidents_party(partie)
                except:
                    print("President not recognized, please try again.")
                filter.clear()
            elif q3.lower() == "2":
                parti = input("""Which party are you searching for?
(Independent, Federalist, Democratic-Republican, Democratic, Whig, Republican) """)
                parties_president(parti)
                filter.clear()
            else:
                print("Input not recognized, please try again.")
        elif q1.lower() == "term":
            year = input("What year are you searching for? ")
            president_year(year)
            filter.clear()
        elif q1.lower() == "picture":
            picture()
            filter.clear()
        elif q1.lower() == "home state":
            homestate()
            filter.clear()
        else:
            print("Input not recognized, please try again.")
    else:
        print("Input not recognized, please try again.")

#Sources
#President Dataset
#Website name: code.org
#URL: https://www.whitehouse.gov/about-the-white-house/presidents/
#Article name: US Presidents

#Presidential Portraits
#Website name: The American Presidency Project
#URL: https://www.presidency.ucsb.edu/presidents
