
total = 0
count = 0
while count < 5:
    usrInput = int(input("Your number please"))
    total += usrInput
    count += 1 # to add so that it will not become an infinite loop
print("While: Total sum is",total)