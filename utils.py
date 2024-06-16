from random import randint  # Import the randint function from the random module
from flask import send_file  # Import the send_file function from the flask module
from io import BytesIO  # Import the BytesIO function from the io module


def generateRandomHex():  # Define a function to generate a random hex code
    return "#%06x" % randint(
        0, 0xFFFFFF
    )  # Generate a random hex code and return it as a string


def serveImage(pilImage):  # Define a function to serve an image
    imageIo = BytesIO()  # Create a BytesIO object
    pilImage.save(imageIo, "PNG", quality=100)  # Save the image to the BytesIO object
    imageIo.seek(0)  # Set the position of the BytesIO object to the beginning
    return send_file(imageIo, mimetype="image/png")  # Return the image as a file
