#Dominic Brogni
#Congestion
#Prints the busiest streets in Chicago

#Init
# Chicago Streets
chicago_streets = [
    "State St", "Michigan Ave", "Wacker Dr", "Lake Shore Dr", "Western Ave",
    "Halsted St", "Milwaukee Ave", "Fullerton Ave", "Grand Ave", "Belmont Ave",
    "Irving Park Rd", "North Ave", "Lawrence Ave", "Foster Ave", "Bryn Mawr Ave",
    "Peterson Ave", "Touhy Ave", "Devon Ave", "Addison St", "Montrose Ave",
    "Damen Ave", "Elston Ave", "Lincoln Ave", "Archer Ave", "Pulaski Rd",
    "Cicero Ave", "Kedzie Ave", "California Ave", "Homan Ave", "Central Park Ave",
    "Narragansett Ave", "Austin Blvd", "Ashland Ave", "Central Ave", "Laramie Ave",
    "Kostner Ave", "Crawford Ave", "Columbus Dr", "LaSalle St", "Dearborn St",
    "Clark St", "Broadway", "Sheridan Rd", "Ridge Ave", "Clybourn Ave",
    "Ogden Ave", "Roosevelt Rd", "Cermak Rd", "Pershing Rd", "Garfield Blvd"
] #Stores high traffic streets across the city

# Traffic Volume (cars recorded per hour)
traffic_volume = [
    2800, 5200, 2900, 2500, 4100,
    2100, 2400, 4800, 1800, 2300,
    2200, 4300, 1900, 1500, 1400,
    2600, 2100, 1700, 2400, 1800,
    2000, 1900, 3900, 2500, 2800,
    2900, 2200, 1600, 1200, 1100,
    1300, 1700, 4500, 2100, 1800,
    1400, 1300, 2900, 2700, 2400,
    2200, 2500, 2600, 2100, 1900,
    2300, 2800, 2400, 2100, 1500
] #Stores the traffic volume of each corresponding street
busiest_streets = [] #Filter to store matching information
#Functions
def congestion(traffic):
    for i in range(len(traffic_volume)):
        if traffic_volume[i] >= traffic:
            busiest_streets.append(chicago_streets[i])
    print(busiest_streets) #Displays streets higher than the provided traffic volume
    most = max(busiest_streets)
    print(most) #Displays the busiest street

#Main
congestion(3000)
