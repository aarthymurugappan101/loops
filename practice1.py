'''
Given a List A=[2,5,3,1,6,8], use for loop and 
if statements to find and print out the even numbers 
in the list. The printed output would be 2 6 8 in this case.
'''

# Pseudo Code
# List contain numbers
# for each number that exist in the List
#   if the number is divisible by 2
#       print(number)

numbers = [3,6,8,9,10,38,2,5,23] # line 8
for number in numbers: # line 9
    if number % 2 == 0: # line 10
        print(number) # carriage line \n aka next line
        # print(number, end=" * ")

