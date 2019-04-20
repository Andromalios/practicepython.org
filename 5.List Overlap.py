#Take two lists, say for example these two:

#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

#Extras:

#Randomly generate two lists to test this
#Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random # importing random library for random.randrange function
#randomly generated lists with random.randrange function
list_a = [x for x in str(random.randrange(1, 100000, 2))] 
list_b = [x for x in str(random.randrange(1, 10000000, 3))]

print([x for x in list_a if x in list_b]) #printing out the numbers that are found in both lists
#verifying lists 
print("List a: " +str(list_a))
print("List b: " +str(list_b))