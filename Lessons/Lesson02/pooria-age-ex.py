print("please enter today's date")

ouryear = input("Enter the year: ")
ouryear = int(ouryear)

ourmonth = input("Enter the month:")
ourmonth = int(ourmonth)

ourday = input("Enter the day:")
ourday = int(ourday)
print("")
print ("please anwer this questions,too")
print("")
age = input("Enter your age please: ")
age = int(age)

shamsimonth = input("in which month did you burn?")
shamsimonth = int(shamsimonth)

day = input("in which day did you burn?")
day = int(day)
print("")
print("You were burn on :" , ouryear-age ,"/",shamsimonth ,"/" , day )
print("you spent", (age*365*24*60*60) + ((ourmonth-shamsimonth)*24*60*60) + ((ourday-day)*60*60) , "seconds until today") 
print("GOOD JOB!")