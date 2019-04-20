# Practicepython.org Exercise 2 - Odd or Even
# Ask the user for a number. 
#Depending on whether the number is even or odd, print out an appropriate message to the user. 
#Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# 1.If the number is a multiple of 4, print out a different message.
# 2.Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#  If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = int(input ("Enter your number:")) #Number input
if (number % 4 == 0): # check if the number is a multiple of 4 
    print("Number is multiple of 4")
if (number % 2 == 0): # check if the number is even
    print("Number is even")
else: # if the number is not even then it must be odd, right?
    print("Number is odd")
number1 = int(input("Enter the first number: ")) #Number input
number2 = int(input("Enter the second number: ")) #Number input
if (number1 % number2 == 0):   #Check if the first number can be divided by the second
    print("First number divides evenly into the second!!!")
else: #if the number can't be divided then it can't be divided
    print("Number does not evenly divide into the second :((( ")