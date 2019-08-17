# Ask the user for an input and display it out, only exits when the user enters 'N'

usrInput = input("Please enter your character: ")
while usrInput != 'N':
    print("You have enter the character: "+usrInput)
    usrInput = input("Please enter your character: ")

print("Out of the loop")