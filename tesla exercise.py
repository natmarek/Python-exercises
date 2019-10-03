def checkDriverAge():age = input("What is your age?: ")
  age=0
  if int(age) < 18:
    return(print("Sorry, you are too yound to drive this car. Powering off"))
  elif int(age) > 18:
    return(print("Powering On. Enjoy the ride!"));
  elif int((age) == 18):
    return(print("Congratulations on your first year of driving. Enjoy the ride!"))

checkDriverAge()
