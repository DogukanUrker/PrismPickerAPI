from random import randint  # Import the randint function from the random module

def generateRandomHex(): # Define a function to generate a random hex code
    return "#%06x" % randint(0, 0xFFFFFF) # Generate a random hex code and return it as a string