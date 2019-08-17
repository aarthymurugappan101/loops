#Read number
userInput = input("Enter a positive int value, 0 to quit : ")

value = int(userInput)
# Keep reading until the input is 0
sumTotal = 0
while value!= 0:
  sumTotal += value

  #Repeat the reading of the next value
  userInput = input("Enter a positive int value, 0 to quit : ")
  value = int(userInput)

print("The sum is",sumTotal)
