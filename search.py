#Dominic Brogni
#Search
#Demonstrate search types through a counting simulation

#Init


#Setup game
import random
secret_num = random.randint(1,100) #creates a number for the robot to guess
print(f"The secret number is: {secret_num}") #Displays the number upon program call for user to see


#Functions


#Linear search function
def linear_search(): #Simulates a linear search for the generated number
    print("|Linear search initializing...|")
    global secret_num
    attempts = 0
    for guess in range(1,101): #Loop searches number by number
        attempts = attempts + 1
        if guess == secret_num:
            print(f"""I found the secret number; it is {secret_num}.
It took me {attempts} attempts to find it.""")


#Binary search function
def binary_search(): #Simulates a binary search for the generated number
    print("|Binary search initializing...|")
    global secret_num
    attempts = 0 #Resets previous attempt count from linear search
    high = 100
    low = 0
    found = False
    while found == False: #Using while False allows for adaptation based on desired high/low variables
        attempts = attempts + 1
        mid = (low + high) // 2 #Using a mid value cuts the range in half
        if mid < secret_num:
            low = mid + 1
        elif mid > secret_num:
            high = mid-1
        elif mid == secret_num:
            print(f"""I found the secret number; it is {secret_num}.
It took me {attempts} attempts to find it.""")
            found = True

#Main
print("-------------------------------------")
linear_search()
print("-------------------------------------")
binary_search()
print("-------------------------------------")
