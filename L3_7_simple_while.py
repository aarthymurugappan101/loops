ctr = 0
while ctr < 10:
  print ("we are at " + str(ctr) , end='' )
  if ctr == 3:
    print(" just started")
  elif ctr == 6:
    print (" half way there")
  elif ctr == 8: 
    print (" almost there")
  else:
    print(" ")
#  ctr=+1
  ctr+=1

print("Finally we are done")