from flask import Flask  # Import the Flask module for creating the API
from converter import HexConverter, RGBConverter, RGBAConverter  # Import the converter module
from utils import generateRandomHex  # Import the generateRandomHex function
from random import randint, choice  # Import the randint and choice functions from the random module
from json import loads  # Import the loads function from the json module

app = Flask(__name__)  # Create a Flask application

@app.get("/")  # Decorator to define the route for the home page
def home(): # Define the home function
    return "Welcome to the Prism Picker API!"  # Return a welcome message when the home page is accessed

@app.get("/convert/hex/rgb/<hexCode>")  # Decorator to define the route for converting hex to RGB
def hexToRgb(hexCode): # Define the hexToRgb function that takes the hex code as an argument
    rgb = HexConverter.hexToRgb(hexCode)  # Call the hexToRgb method from the HexConverter class
    return {"rgb": rgb}  # Return the RGB value as a JSON object

@app.get("/convert/hex/rgba/<hexCode>/<alpha>")  # Decorator to define the route for converting hex to RGBA
def hexToRgba(hexCode, alpha): # Define the hexToRgba function that takes the hex code and alpha value as arguments
    rgba = HexConverter.hexToRgba(hexCode, float(alpha))  # Call the hexToRgba method from the HexConverter class
    return {"rgba": rgba}  # Return the RGBA value as a JSON object

@app.get("/convert/rgb/hex/<r>/<g>/<b>")  # Decorator to define the route for converting RGB to hex
def rgbToHex(r, g, b): # Define the rgbToHex function that takes the RGB values as arguments
    rgb = (int(r), int(g), int(b))  # Convert the RGB values to integers
    hexCode = RGBConverter.rgbToHex(rgb)  # Call the rgbToHex method from the RGBConverter class
    return {"hex": hexCode}  # Return the hex code as a JSON object

@app.get("/convert/rgb/rgba/<r>/<g>/<b>/<alpha>")  # Decorator to define the route for converting RGB to RGBA
def rgbToRgba(r, g, b, alpha): # Define the rgbToRgba function that takes the RGB values as arguments
    rgb = (int(r), int(g), int(b))  # Convert the RGB values to integers
    rgba = RGBConverter.rgbToRgba(rgb, float(alpha))  # Call the rgbToRgba method from the RGBConverter class
    return {"rgba": rgba}  # Return the RGBA value as a JSON object

@app.get("/convert/rgba/rgb/<r>/<g>/<b>/<alpha>")  # Decorator to define the route for converting RGBA to RGB
def rgbaToRgb(r, g, b, alpha): # Define the rgbaToRgb function that takes the RGBA values as arguments
    rgba = (int(r), int(g), int(b), float(alpha))  # Convert the RGBA values to integers and float
    rgb = RGBAConverter.rgbaToRgb(rgba)  # Call the rgbaToRgb method from the RGBAConverter class
    return {"rgb": rgb}  # Return the RGB value as a JSON object

@app.get("/convert/rgba/hex/<r>/<g>/<b>/<alpha>")  # Decorator to define the route for converting RGBA to hex
def rgbaToHex(r, g, b, alpha):  # Define the rgbaToHex function that takes the RGBA values as arguments
    rgba = (int(r), int(g), int(b), float(alpha))  # Convert the RGBA values to integers and float
    hexCode = RGBAConverter.rgbaToHex(rgba)  # Call the rgbaToHex method from the RGBAConverter class
    return {"hex": hexCode}  # Return the hex code as a JSON object

@app.get("/random/hex")  # Decorator to define the route for generating a random hex code
def randomHex(): # Define the randomHex function
    hexCode = generateRandomHex() # Generate a random hex code
    return {"hex": hexCode}  # Return the hex code as a JSON object

@app.get("/random/rgb")  # Decorator to define the route for generating a random RGB value
def randomRgb(): # Define the randomRgb function
    hexCode = generateRandomHex() # Generate a random hex code
    rgb = HexConverter.hexToRgb(hexCode)   # Convert the hex code to RGB values
    return {"rgb": rgb} # Return the RGB value as a JSON object

@app.get("/random/rgba/")  # Decorator to define the route for generating a random RGBA value
def randomRgba(): # Define the randomRgba function
    hexCode = generateRandomHex() # Generate a random hex code
    rgba = HexConverter.hexToRgba(hexCode, randint(1,10) / 10) # Convert the hex code to RGBA values
    return {"rgba": rgba} # Return the RGBA value as a JSON object

@app.get("/random")  # Decorator to define the route for generating a random color value
def randomColor(): # Define the randomColor function
    hexCode = generateRandomHex() # Generate a random hex code
    rgb = HexConverter.hexToRgb(hexCode) # Generate a random hex code and convert it to RGB values
    rgba = HexConverter.hexToRgba(hexCode, randint(1,10) / 10) # Generate a random hex code, RGB, and RGBA values
    return {"hex": hexCode, "rgb": rgb, "rgba": rgba} # Return the hex code, RGB, and RGBA values as a JSON object

@app.get("/random/hex/<count>")  # Decorator to define the route for generating multiple random hex codes
def randomHexes(count): # Define the randomHexes function that takes the count as an argument
    hexCodes = [generateRandomHex() for _ in range(int(count))] # Generate multiple random hex codes
    return {"hex": hexCodes} # Return the hex codes as a JSON object

@app.get("/random/rgb/<count>")  # Decorator to define the route for generating multiple random RGB values
def randomRgbs(count): # Define the randomRgbs function that takes the count as an argument
    hexCodes = [generateRandomHex() for _ in range(int(count))] # Generate multiple random hex codes
    rgbs = [HexConverter.hexToRgb(hexCode) for hexCode in hexCodes] # Convert the hex codes to RGB values
    return {"rgb": rgbs} # Return the RGB values as a JSON object

@app.get("/random/rgba/<count>")  # Decorator to define the route for generating multiple random RGBA values
def randomRgbas(count): # Define the randomRgbas function that takes the count as an argument
    hexCodes = [generateRandomHex() for _ in range(int(count))] # Generate multiple random hex codes
    rgbas = [HexConverter.hexToRgba(hexCode, randint(1,10) / 10) for hexCode in hexCodes] # Convert the hex codes to RGBA values
    return {"rgba": rgbas} # Return the RGBA values as a JSON object

@app.get("/random/<count>")  # Decorator to define the route for generating multiple random color values
def randomColors(count): # Define the randomColors function that takes the count as an argument
    hexCodes = [generateRandomHex() for _ in range(int(count))] # Generate multiple random hex codes
    rgbs = [HexConverter.hexToRgb(hexCode) for hexCode in hexCodes] # Convert the hex codes to RGB values
    rgbas = [HexConverter.hexToRgba(hexCode, randint(1,10) / 10) for hexCode in hexCodes] # Convert the hex codes to RGBA values
    return {"hex": hexCodes, "rgb": rgbs, "rgba": rgbas} # Return the hex codes, RGB, and RGBA values as a JSON object

@app.get("/tailwind")  # Decorator to define the route for returns all the tailwind colors
def tailwind(): # Define the tailwind function
    file = open("colors/tailwind.json", "r") # Open the tailwind.json file in read mode
    colors = loads(file.read()) # Read the contents of the file and parse it as JSON
    return colors # Return the colors as a JSON object

@app.get("/tailwind/<color>")  # Decorator to define the route for returning a specific tailwind color
def tailwindColor(color): # Define the tailwindColor function that takes the color name as an argument
    color = color.lower() # Convert the color name to lowercase
    file = open("colors/tailwind.json", "r") # Open the tailwind.json file in read mode
    colors = loads(file.read()) # Read the contents of the file and parse it as JSON
    return colors.get(color, {"Message": f"Color '{color}' not found."}) # Return the color if found, else return a message
 
@app.get("/tailwind/random")  # Decorator to define the route for generating a random tailwind color
def randomTailwind(): # Define the randomTailwind function
    file = open("colors/tailwind.json", "r") # Open the tailwind.json file in read mode
    colors = loads(file.read()) # Read the contents of the file and parse it as JSON
    randomColor = choice(list(colors.keys())) # Select a random color from the list of tailwind colors
    return colors[randomColor] # Return the random color as a JSON object
    
@app.get("/tailwind/random/<count>")  # Decorator to define the route for generating multiple random tailwind colors
def randomTailwinds(count): # Define the randomTailwinds function that takes the count as an argument
    file = open("colors/tailwind.json", "r") # Open the tailwind.json file in read mode
    colors = loads(file.read()) # Read the contents of the file and parse it as JSON
    randomColors = [colors[choice(list(colors.keys()))] for _ in range(int(count))] # Select multiple random colors from the list of tailwind colors
    return randomColors # Return the random colors as a JSON object


if __name__ == "__main__": # Check if the script is executed directly
    app.run(debug=True)  # Run the Flask application in debug mode if the script is executed directly
