#Take a list, say for example this one:

#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
#Extras:

#Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] # List provided
number = int(input("Insert number to compare: ")) #Input for the comparison number
print([item for item in list if item < number]) #Printing the list, basically print the item that is in the list if the item is smaller than the number provided for comparison