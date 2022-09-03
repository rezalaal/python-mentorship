# Start Program with Hello
print("hi")

# Give the user's name
name = input("Enter your name : ")
# Print the user's name on screen
print("hello", name)

# Give the user's age
YourBirthYear = input("Enter YourBirthYear :")
# Convert the user's age to an integer
YourBirthYear = int(YourBirthYear)

# Give current year from user
thisYear = input("Enter thisYear:  ")
# Convert the current year to an integer
thisYear = int(thisYear)

# Calculate the user's age
age = thisYear-YourBirthYear

# Print the user's age and it's name on screen
print("your age is:", age, name)