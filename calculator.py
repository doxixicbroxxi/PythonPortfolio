#Dominic Brogni
#calculator
#Asks user to provide 2 #s and an operation, and prints the result

#Init
#Functions
def main():
    #Welcome Message
    print("Welcome to Calc (short for calculator btw)")

    #Collect Inputs
    numb1 = int(input("Please enter the first number: "))
    numb2 = int(input("Please enter the second number: "))
    operator = input("Please enter a simple operation(+,-,*,/): ")

    #Perform Operations
    if operator == "+":
        print(calc_sum(numb1, numb2))
    elif operator == "-":
        print(calc_sub(numb1, numb2))
    elif operator == "*":
        print(calc_mult(numb1, numb2))
    elif operator == "/":
        print(calc_div(numb1, numb2))

def calc_sum(numb1, numb2):
    sum = numb1 + numb2
    return sum
def calc_sub(numb1, numb2):
    sub = numb1 - numb2
    return sub
def calc_div(numb1, numb2):
    div = numb1 / numb2
    return div
def calc_mult(numb1, numb2):
    mult = numb1 * numb2
    return mult
#Main
main()
