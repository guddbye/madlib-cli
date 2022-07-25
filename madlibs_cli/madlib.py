# Print a welcome message to the user, explaining the Madlib process and command line interactions.
print("Welcome to the Madlib program.")
print("This program will take a template and fill in the blanks with user input.")
print("You will be prompted to enter a series of words to fill in the blanks.")
print("When you are done, the program will print the completed Madlib.")

print("********************************************************************************")
print("                                                                               ")

print("It is time for Madlib")

def read_template (path):
    file = open(path, "r")
    read = file.read()
    file.close()
    return read.strip()

print("Please enter an adjective:")
adjective1 = input("Adjective: ", )
print("Please enter an adjective:")
adjective2 = input("Adjective: ")
print("Please enter a noun:")
noun = input("Noun: ")

# Read a template Madlib file (Example), and parse that file into usable parts.
print("It was a " + adjective1 + " and " + adjective2 + " " + noun + ".")