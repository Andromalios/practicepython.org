#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
number = int(input("Insert number to check if dividable: ")) #User input to check if number can be divided
list = range(1, 27) #Created a list from 1 to 26
print([item for item in list if number % item == 0]) #the program will print out the values that when divided by an item in the list have the remainder 0