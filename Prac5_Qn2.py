'''
 Create a List list1 that stores Integers.
 The program will repeatedly receive input from keyboard and add it to the List
until the user enters N.
 After retrieval is done, use a for loop to retrieve the largest number from the List
and print it out.
 Use another loop to find the 2 nd largest number from the List and print it out.
'''
# initialize list1 = [] of integers
# while user input is not N
#   take user input and store into list1 # assume the inputs will be Integer
#
# for loop to loop through list1
#   if current number is bigger than stored number
#       save the current number as the largest number
# print out largest number
#
# for loop to loop through list1
#   if current number is bigger than stored number and current number lesser than the largest number
#       save the current number as the second largest number
# print out 2nd largest number

list1 = []
usrInput = input("Enter a number or N to exit ")
while usrInput != "N":
    list1.append(int(usrInput))
    usrInput = input("Enter a number or N to exit ")

largest_number = 0
for current_number in list1:
    if current_number > largest_number:
        largest_number = current_number
# largest_number = max(list1)
print("Largest Number:", largest_number) 

second_largest_number = 0
for current_number in list1:
    if current_number > second_largest_number and current_number < largest_number:
        second_largest_number = current_number
print("Second Largest Number:", second_largest_number)