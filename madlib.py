# Print a welcome message to the user, explaining the Madlib process and command line interactions.
print("Welcome to the Madlib program.")
print("This program will take a template and fill in the blanks with user input.")
print("You will be prompted to enter a series of words to fill in the blanks.")
print("When you are done, the program will print the completed Madlib.")

print("********************************************************************************")
print("                                                                               ")

while True:
    print("Please enter an adjective:")
    adjective1 = input("Adjective: ", )
    print("Please enter an adjective:")
    adjective2 = input("Adjective: ")
    print("Please enter a noun:")
    noun = input("Noun: ")

# Read a template Madlib file (Example), and parse that file into usable parts.
print("It was a " + adjective1 + " and " + adjective2 + " " + noun + ".")

# Prompt the user to continue or quit.
again = input("Would you like to continue? (y/n) ")


def again():
    if again == "y":
        again()

    elif again == "n":
        print("Thank you for using the Madlib program.")
        print("Goodbye!")
    else:
        print("Please enter a valid response.")
