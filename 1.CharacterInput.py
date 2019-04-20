# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Import date 
import datetime
now = datetime.datetime.now() 
#Name input
name = str( input("What is your name? "))
#Age input
age = int( input("Hey "+ name + ". What is your age? "))
#How many years until 100
years_until_100 = 100 - age
# Print out in how many years they will be 100
print("Hello, "+name+", you will be 100 in ",(now.year+years_until_100))