from flask import Flask  # Import the Flask module for creating the API
from converter import HexConverter, RGBConverter, RGBAConverter  # Import the converter module
from utils import generateRandomHex  # Import the generateRandomHex function
from random import randint  # Import the randint function from the random module

app = Flask(__name__)  # Create a Flask application

@app.get("/")  # Decorator to define the route for the home page
def home():
    return "Welcome to the Prism Picker API!"  # Return a welcome message when the home page is accessed

@app.get("/convert/hex/rgb/<hexCode>")  # Decorator to define the route for converting hex to RGB
def hexToRgb(hexCode):
    rgb = HexConverter.hexToRgb(hexCode)  # Call the hexToRgb method from the HexConverter class
    return {"rgb": rgb}  # Return the RGB value as a JSON object

@app.get("/convert/hex/rgba/<hexCode>/<alpha>")  # Decorator to define the route for converting hex to RGBA
def hexToRgba(hexCode, alpha):
    rgba = HexConverter.hexToRgba(hexCode, float(alpha))  # Call the hexToRgba method from the HexConverter class
    return {"rgba": rgba}  # Return the RGBA value as a JSON object

@app.get("/convert/rgb/hex/<r>/<g>/<b>")  # Decorator to define the route for converting RGB to hex
def rgbToHex(r, g, b):
    rgb = (int(r), int(g), int(b))  # Convert the RGB values to integers
    hexCode = RGBConverter.rgbToHex(rgb)  # Call the rgbToHex method from the RGBConverter class
    return {"hex": hexCode}  # Return the hex code as a JSON object

@app.get("/convert/rgb/rgba/<r>/<g>/<b>/<alpha>")  # Decorator to define the route for converting RGB to RGBA
def rgbToRgba(r, g, b, alpha):
    rgb = (int(r), int(g), int(b))  # Convert the RGB values to integers
    rgba = RGBConverter.rgbToRgba(rgb, float(alpha))  # Call the rgbToRgba method from the RGBConverter class
    return {"rgba": rgba}  # Return the RGBA value as a JSON object

@app.get("/convert/rgba/rgb/<r>/<g>/<b>/<alpha>")  # Decorator to define the route for converting RGBA to RGB
def rgbaToRgb(r, g, b, alpha):
    rgba = (int(r), int(g), int(b), float(alpha))  # Convert the RGBA values to integers and float
    rgb = RGBAConverter.rgbaToRgb(rgba)  # Call the rgbaToRgb method from the RGBAConverter class
    return {"rgb": rgb}  # Return the RGB value as a JSON object

@app.get("/convert/rgba/hex/<r>/<g>/<b>/<alpha>")  # Decorator to define the route for converting RGBA to hex
def rgbaToHex(r, g, b, alpha):
    rgba = (int(r), int(g), int(b), float(alpha))  # Convert the RGBA values to integers and float
    hexCode = RGBAConverter.rgbaToHex(rgba)  # Call the rgbaToHex method from the RGBAConverter class
    return {"hex": hexCode}  # Return the hex code as a JSON object

@app.get("/random/hex")  # Decorator to define the route for generating a random hex code
def randomHex():
    hexCode = generateRandomHex() # Generate a random hex code
    return {"hex": hexCode}  # Return the hex code as a JSON object

@app.get("/random/rgb")  # Decorator to define the route for generating a random RGB value
def randomRgb():
    hexCode = generateRandomHex() # Generate a random hex code
    rgb = HexConverter.hexToRgb(hexCode)   # Convert the hex code to RGB values
    return {"rgb": rgb} # Return the RGB value as a JSON object

@app.get("/random/rgba/")  # Decorator to define the route for generating a random RGBA value
def randomRgba():
    hexCode = generateRandomHex() # Generate a random hex code
    rgba = HexConverter.hexToRgba(hexCode, randint(1,10) / 10) # Convert the hex code to RGBA values
    return {"rgba": rgba} # Return the RGBA value as a JSON object


if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask application in debug mode if the script is executed directly
