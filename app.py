from flask import Flask  # Import the Flask class from the flask module
from flask import request  # Import the request object from the flask module
from converter import (
    HexConverter,  # Import the HexConverter class
    RGBConverter,  # Import the RGBConverter class
    RGBAConverter,  # Import the RGBAConverter class
)  # Import the converter module
from utils import generateRandomHex  # Import the generateRandomHex function
from utils import serveImage  # Import the serveImage function
from random import (  # Import the random module to generate random values
    randint,  # Import the randint function to generate random integers
    choice,  # Import the choice function to select a random item from a list
)  # Import the randint and choice functions from the random module
from json import loads  # Import the loads function from the json module
from PIL import Image  # Import the Image class from the PIL module

app = Flask(__name__)  # Create a Flask application


@app.get("/")  # Decorator to define the route for the home page
def home():  # Define the home function
    return "Welcome to the Prism Picker API!"  # Return a welcome message when the home page is accessed


@app.errorhandler(404)  # Decorator to define the route for handling 404 errors
def page_not_found(
    e,
):  # Define the page_not_found function that takes the error as an argument
    return {
        e.name: e.description
    }, 404  # Return the error message and status code as a JSON object


@app.get(
    "/convert/hex/rgb/<hexCode>"
)  # Decorator to define the route for converting hex to RGB
def hexToRgb(
    hexCode,
):  # Define the hexToRgb function that takes the hex code as an argument
    rgb = HexConverter.hexToRgb(
        hexCode
    )  # Call the hexToRgb method from the HexConverter class
    return {"rgb": rgb}  # Return the RGB value as a JSON object


@app.get(
    "/convert/hex/rgba/<hexCode>/<alpha>"
)  # Decorator to define the route for converting hex to RGBA
def hexToRgba(
    hexCode, alpha
):  # Define the hexToRgba function that takes the hex code and alpha value as arguments
    rgba = HexConverter.hexToRgba(
        hexCode, float(alpha)
    )  # Call the hexToRgba method from the HexConverter class
    return {"rgba": rgba}  # Return the RGBA value as a JSON object


@app.get(
    "/convert/rgb/hex/<r>/<g>/<b>"
)  # Decorator to define the route for converting RGB to hex
def rgbToHex(
    r, g, b
):  # Define the rgbToHex function that takes the RGB values as arguments
    rgb = (int(r), int(g), int(b))  # Convert the RGB values to integers
    hexCode = RGBConverter.rgbToHex(
        rgb
    )  # Call the rgbToHex method from the RGBConverter class
    return {"hex": hexCode}  # Return the hex code as a JSON object


@app.get(
    "/convert/rgb/rgba/<r>/<g>/<b>/<alpha>"
)  # Decorator to define the route for converting RGB to RGBA
def rgbToRgba(
    r, g, b, alpha
):  # Define the rgbToRgba function that takes the RGB values as arguments
    rgb = (int(r), int(g), int(b))  # Convert the RGB values to integers
    rgba = RGBConverter.rgbToRgba(
        rgb, float(alpha)
    )  # Call the rgbToRgba method from the RGBConverter class
    return {"rgba": rgba}  # Return the RGBA value as a JSON object


@app.get(
    "/convert/rgba/rgb/<r>/<g>/<b>/<alpha>"
)  # Decorator to define the route for converting RGBA to RGB
def rgbaToRgb(
    r, g, b, alpha
):  # Define the rgbaToRgb function that takes the RGBA values as arguments
    rgba = (
        int(r),
        int(g),
        int(b),
        float(alpha),
    )  # Convert the RGBA values to integers and float
    rgb = RGBAConverter.rgbaToRgb(
        rgba
    )  # Call the rgbaToRgb method from the RGBAConverter class
    return {"rgb": rgb}  # Return the RGB value as a JSON object


@app.get(
    "/convert/rgba/hex/<r>/<g>/<b>/<alpha>"
)  # Decorator to define the route for converting RGBA to hex
def rgbaToHex(
    r, g, b, alpha
):  # Define the rgbaToHex function that takes the RGBA values as arguments
    rgba = (
        int(r),
        int(g),
        int(b),
        float(alpha),
    )  # Convert the RGBA values to integers and float
    hexCode = RGBAConverter.rgbaToHex(
        rgba
    )  # Call the rgbaToHex method from the RGBAConverter class
    return {"hex": hexCode}  # Return the hex code as a JSON object


@app.get(
    "/random/hex"
)  # Decorator to define the route for generating a random hex code
def randomHex():  # Define the randomHex function
    hexCode = generateRandomHex()  # Generate a random hex code
    return {"hex": hexCode}  # Return the hex code as a JSON object


@app.get(
    "/random/rgb"
)  # Decorator to define the route for generating a random RGB value
def randomRgb():  # Define the randomRgb function
    hexCode = generateRandomHex()  # Generate a random hex code
    rgb = HexConverter.hexToRgb(hexCode)  # Convert the hex code to RGB values
    return {"rgb": rgb}  # Return the RGB value as a JSON object


@app.get(
    "/random/rgba/"
)  # Decorator to define the route for generating a random RGBA value
def randomRgba():  # Define the randomRgba function
    hexCode = generateRandomHex()  # Generate a random hex code
    rgba = HexConverter.hexToRgba(
        hexCode, randint(1, 10) / 10
    )  # Convert the hex code to RGBA values
    return {"rgba": rgba}  # Return the RGBA value as a JSON object


@app.get("/random")  # Decorator to define the route for generating a random color value
def randomColor():  # Define the randomColor function
    hexCode = generateRandomHex()  # Generate a random hex code
    rgb = HexConverter.hexToRgb(
        hexCode
    )  # Generate a random hex code and convert it to RGB values
    rgba = HexConverter.hexToRgba(
        hexCode, randint(1, 10) / 10
    )  # Generate a random hex code, RGB, and RGBA values
    return {
        "hex": hexCode,
        "rgb": rgb,
        "rgba": rgba,
    }  # Return the hex code, RGB, and RGBA values as a JSON object


@app.get(
    "/random/hex/<count>"
)  # Decorator to define the route for generating multiple random hex codes
def randomHexes(
    count,
):  # Define the randomHexes function that takes the count as an argument
    hexCodes = [
        generateRandomHex() for _ in range(int(count))
    ]  # Generate multiple random hex codes
    return {"hex": hexCodes}  # Return the hex codes as a JSON object


@app.get(
    "/random/rgb/<count>"
)  # Decorator to define the route for generating multiple random RGB values
def randomRgbs(
    count,
):  # Define the randomRgbs function that takes the count as an argument
    hexCodes = [
        generateRandomHex() for _ in range(int(count))
    ]  # Generate multiple random hex codes
    rgbs = [
        HexConverter.hexToRgb(hexCode) for hexCode in hexCodes
    ]  # Convert the hex codes to RGB values
    return {"rgb": rgbs}  # Return the RGB values as a JSON object


@app.get(
    "/random/rgba/<count>"
)  # Decorator to define the route for generating multiple random RGBA values
def randomRgbas(
    count,
):  # Define the randomRgbas function that takes the count as an argument
    hexCodes = [
        generateRandomHex() for _ in range(int(count))
    ]  # Generate multiple random hex codes
    rgbas = [
        HexConverter.hexToRgba(hexCode, randint(1, 10) / 10) for hexCode in hexCodes
    ]  # Convert the hex codes to RGBA values
    return {"rgba": rgbas}  # Return the RGBA values as a JSON object


@app.get(
    "/random/<count>"
)  # Decorator to define the route for generating multiple random color values
def randomColors(
    count,
):  # Define the randomColors function that takes the count as an argument
    hexCodes = [
        generateRandomHex() for _ in range(int(count))
    ]  # Generate multiple random hex codes
    rgbs = [
        HexConverter.hexToRgb(hexCode) for hexCode in hexCodes
    ]  # Convert the hex codes to RGB values
    rgbas = [
        HexConverter.hexToRgba(hexCode, randint(1, 10) / 10) for hexCode in hexCodes
    ]  # Convert the hex codes to RGBA values
    return {
        "hex": hexCodes,
        "rgb": rgbs,
        "rgba": rgbas,
    }  # Return the hex codes, RGB, and RGBA values as a JSON object


@app.get(
    "/tailwind"
)  # Decorator to define the route for returns all the tailwind colors
def tailwind():  # Define the tailwind function
    file = open("colors/tailwind.json", "r")  # Open the tailwind.json file in read mode
    colors = loads(file.read())  # Read the contents of the file and parse it as JSON
    return colors  # Return the colors as a JSON object


@app.get(
    "/tailwind/<color>"
)  # Decorator to define the route for returning a specific tailwind color
def tailwindColor(
    color,
):  # Define the tailwindColor function that takes the color name as an argument
    color = color.lower()  # Convert the color name to lowercase
    file = open("colors/tailwind.json", "r")  # Open the tailwind.json file in read mode
    colors = loads(file.read())  # Read the contents of the file and parse it as JSON
    return colors.get(
        color, {"Message": f"Color '{color}' not found."}
    )  # Return the color if found, else return a message


@app.get(
    "/tailwind/random"
)  # Decorator to define the route for generating a random tailwind color
def randomTailwind():  # Define the randomTailwind function
    file = open("colors/tailwind.json", "r")  # Open the tailwind.json file in read mode
    colors = loads(file.read())  # Read the contents of the file and parse it as JSON
    randomColor = choice(
        list(colors.keys())
    )  # Select a random color from the list of tailwind colors
    return colors[randomColor]  # Return the random color as a JSON object


@app.get(
    "/tailwind/random/<count>"
)  # Decorator to define the route for generating multiple random tailwind colors
def randomTailwinds(
    count,
):  # Define the randomTailwinds function that takes the count as an argument
    file = open("colors/tailwind.json", "r")  # Open the tailwind.json file in read mode
    colors = loads(file.read())  # Read the contents of the file and parse it as JSON
    randomColors = [
        colors[choice(list(colors.keys()))] for _ in range(int(count))
    ]  # Select multiple random colors from the list of tailwind colors
    return randomColors  # Return the random colors as a JSON object


@app.get(
    "/tailwind/random/hex"
)  # Decorator to define the route for generating a random tailwind hex code
def randomTailwindHex():  # Define the randomTailwindHex function
    tones = [
        "50",
        "100",
        "200",
        "300",
        "400",
        "500",
        "600",
        "700",
        "800",
        "900",
        "950",
    ]  # Define the list of tones
    file = open("colors/tailwind.json", "r")  # Open the tailwind.json file in read mode
    colors = loads(file.read())  # Read the contents of the file and parse it as JSON
    randomColor = choice(
        list(colors.keys())
    )  # Select a random color from the list of tailwind colors
    return {
        "hex": colors[randomColor][choice(tones)]
    }  # Return the random hex code as a JSON object


@app.get(
    "/tailwind/random/rgb"
)  # Decorator to define the route for generating a random tailwind RGB value
def randomTailwindRgb():  # Define the randomTailwindRgb function
    tones = [
        "50",
        "100",
        "200",
        "300",
        "400",
        "500",
        "600",
        "700",
        "800",
        "900",
        "950",
    ]  # Define the list of tones
    file = open("colors/tailwind.json", "r")  # Open the tailwind.json file in read mode
    colors = loads(file.read())  # Read the contents of the file and parse it as JSON
    randomColor = choice(
        list(colors.keys())
    )  # Select a random color from the list of tailwind colors
    hexCode = colors[randomColor][choice(tones)]  # Select a random tone for the color
    rgb = HexConverter.hexToRgb(hexCode)  # Convert the hex code to RGB values
    return {"rgb": rgb}  # Return the RGB value as a JSON object


@app.get(
    "/tailwind/random/hex/<count>"
)  # Decorator to define the route for generating multiple random tailwind hex codes
def randomTailwindHexes(
    count,
):  # Define the randomTailwindHexes function that takes the count as an argument
    tones = [
        "50",
        "100",
        "200",
        "300",
        "400",
        "500",
        "600",
        "700",
        "800",
        "900",
        "950",
    ]  # Define the list of tones
    file = open("colors/tailwind.json", "r")  # Open the tailwind.json file in read mode
    colors = loads(file.read())  # Read the contents of the file and parse it as JSON
    hexCodes = [
        colors[choice(list(colors.keys()))][choice(tones)] for _ in range(int(count))
    ]  # Select multiple random hex codes from the list of tailwind colors
    return {"hex": hexCodes}  # Return the hex codes as a JSON object


@app.get(
    "/tailwind/random/rgb/<count>"
)  # Decorator to define the route for generating multiple random tailwind RGB values
def randomTailwindRgbs(
    count,
):  # Define the randomTailwindRgbs function that takes the count as an argument
    tones = [
        "50",
        "100",
        "200",
        "300",
        "400",
        "500",
        "600",
        "700",
        "800",
        "900",
        "950",
    ]  # Define the list of tones
    file = open("colors/tailwind.json", "r")  # Open the tailwind.json file in read mode
    colors = loads(file.read())  # Read the contents of the file and parse it as JSON
    hexCodes = [
        colors[choice(list(colors.keys()))][choice(tones)] for _ in range(int(count))
    ]  # Select multiple random hex codes from the list of tailwind colors
    rgbs = [
        HexConverter.hexToRgb(hexCode) for hexCode in hexCodes
    ]  # Convert the hex codes to RGB values
    return {"rgb": rgbs}  # Return the RGB values as a JSON object


@app.route(
    "/mixer/rgb/<r1>/<g1>/<b1>/<r2>/<g2>/<b2>"
)  # Decorator to define the route for mixing two RGB colors
def mix2Rgb(
    r1, g1, b1, r2, g2, b2
):  # Define the mixRgb function that takes the RGB values of two colors as arguments
    rgb1 = (int(r1), int(g1), int(b1))  # Convert the RGB values to integers
    rgb2 = (int(r2), int(g2), int(b2))  # Convert the RGB values to integers
    mixed = tuple(
        int((rgb1[i] + rgb2[i]) / 2) for i in range(3)
    )  # Calculate the average of the RGB values
    return {"rgb": mixed}  # Return the mixed RGB value as a JSON object


@app.route(
    "/mixer/rgba/<r1>/<g1>/<b1>/<a1>/<r2>/<g2>/<b2>/<a2>"
)  # Decorator to define the route for mixing two RGBA colors
def mix2Rgba(
    r1, g1, b1, a1, r2, g2, b2, a2
):  # Define the mixRgba function that takes the RGBA values of two colors as arguments
    rgba1 = (
        int(r1),
        int(g1),
        int(b1),
        float(a1),
    )  # Convert the RGB values to integers and the alpha value to a float
    rgba2 = (
        int(r2),
        int(g2),
        int(b2),
        float(a2),
    )  # Convert the RGB values to integers and the alpha value to a float
    mixed = tuple(int((rgba1[i] + rgba2[i]) / 2) for i in range(3)) + (
        (rgba1[3] + rgba2[3]) / 2,
    )  # Calculate the average of the RGB values and the alpha values
    return {"rgba": mixed}  # Return the mixed RGBA value as a JSON object


@app.route(
    "/mixer/hex/<hex1>/<hex2>"
)  # Decorator to define the route for mixing two hex colors
def mix2Hex(
    hex1, hex2
):  # Define the mixHex function that takes the hex codes of two colors as arguments
    rgb1 = HexConverter.hexToRgb(hex1)  # Convert the first hex code to RGB values
    rgb2 = HexConverter.hexToRgb(hex2)  # Convert the second hex code to RGB values
    mixed = tuple(
        int((rgb1[i] + rgb2[i]) / 2) for i in range(3)
    )  # Calculate the average of the RGB values
    return {
        "hex": RGBConverter.rgbToHex(mixed)
    }  # Return the mixed hex code as a JSON object


@app.route(
    "/mixer/hex", methods=["GET"]
)  # Decorator to define the route for mixing multiple hex colors
def hexMixer():  # Define the hexMixer function
    colors = request.args.getlist(
        "color"
    )  # Get the list of colors from the query parameters
    if len(colors) < 2:  # Check if there are at least two colors
        return {
            "Bad Request": "Please provide at least two colors"
        }, 400  # Return an error message if less than two colors are provided

    rgbValues = []  # Initialize an empty list to store the RGB values
    for color in colors:  # Iterate over the list of colors
        rgb = HexConverter.hexToRgb(color)  # Convert the hex code to RGB values
        if rgb:  # Check if the RGB values are valid
            rgbValues.append(rgb)  # Add the RGB values to the list

    if len(rgbValues) < 2:  # Check if there are at least two valid RGB values
        return {
            "Bad Request": "Invalid color(s) provided"
        }, 400  # Return an error message if less than two valid RGB values are provided

    mixed = [
        sum(channel) // len(rgbValues) for channel in zip(*rgbValues)
    ]  # Calculate the average of the RGB values
    mixedHex = RGBConverter.rgbToHex(
        mixed
    )  # Convert the mixed RGB values to a hex code

    return {"hex": mixedHex}  # Return the mixed hex code as a JSON object


@app.route(
    "/mixer/rgb", methods=["GET"]
)  # Decorator to define the route for mixing multiple RGB colors
def rgbMixer():  # Define the rgbMixer function
    colors = request.args.getlist(
        "color"
    )  # Get the list of colors from the query parameters
    if len(colors) < 2:  # Check if there are at least two colors
        return {
            "Bad Request": "Please provide at least two colors"
        }, 400  # Return an error message if less than two colors are provided

    rgbValues = []  # Initialize an empty list to store the RGB values
    for color in colors:  # Iterate over the list of colors
        rgb = [
            int(c) for c in color.split(",")
        ]  # Convert the color string to a list of integers
        if len(rgb) != 3 or any(
            c < 0 or c > 255 for c in rgb
        ):  # Check if the RGB values are valid
            return {
                "Bad Request": "Invalid color(s) provided"
            }, 400  # Return an error message if the RGB values are invalid
        rgbValues.append(rgb)  # Add the RGB values to the list

    if len(rgbValues) < 2:  # Check if there are at least two valid RGB values
        return {
            "Bad Request": "Invalid color(s) provided"
        }, 400  # Return an error message if less than two valid RGB values are provided

    mixed = [
        sum(channel) // len(rgbValues) for channel in zip(*rgbValues)
    ]  # Calculate the average of the RGB values

    return {"rgb": mixed}  # Return the mixed RGB values as a JSON object


@app.route(
    "/mixer/rgba", methods=["GET"]
)  # Decorator to define the route for mixing multiple RGBA colors
def rgbaMixer():  # Define the rgbaMixer function
    colors = request.args.getlist(
        "color"
    )  # Get the list of colors from the query parameters
    if len(colors) < 2:  # Check if there are at least two colors
        return {
            "Bad Request": "Please provide at least two colors"
        }, 400  # Return an error message if less than two colors are provided

    rgbaValues = []  # Initialize an empty list to store the RGBA values
    for color in colors:  # Iterate over the list of colors
        rgba = [
            float(c) for c in color.split(",")
        ]  # Convert the color string to a list of floats
        if len(rgba) != 4 or any(
            c < 0 or c > 1 for c in rgba
        ):  # Check if the RGBA values are valid
            return {
                "Bad Request": "Invalid color(s) provided"
            }, 400  # Return an error message if the RGBA values are invalid
        rgbaValues.append(rgba)  # Add the RGBA values to the list

    if len(rgbaValues) < 2:  # Check if there are at least two valid RGBA values
        return {
            "Bad Request": "Invalid color(s) provided"
        }, 400  # Return an error message if less than two valid RGBA values are provided

    mixed = [
        sum(channel) / len(rgbaValues) for channel in zip(*rgbaValues)
    ]  # Calculate the average of the RGBA values

    return {"rgba": mixed}  # Return the mixed RGBA values as a JSON object


@app.route(
    "/image/rgb/<r>/<g>/<b>/<w>/<h>"
)  # Decorator to define the route for generating an image with RGB color
def imageRgb(
    r, g, b, w, h
):  # Define the imageRgb function that takes the RGB values and dimensions as arguments
    rgb = (int(r), int(g), int(b))  # Convert the RGB values to integers
    img = Image.new(
        "RGB", (int(w), int(h)), rgb
    )  # Create a new RGB image with the specified dimensions and color
    return serveImage(img)  # Return the image as a response


@app.route(
    "/image/hex/<hex>/<w>/<h>"
)  # Decorator to define the route for generating an image with hex color
def imageHex(
    hex, w, h
):  # Define the imageHex function that takes the hex code and dimensions as arguments
    rgb = HexConverter.hexToRgb(hex)  # Convert the hex code to RGB values
    img = Image.new(
        "RGB", (int(w), int(h)), rgb
    )  # Create a new RGB image with the specified dimensions and color
    return serveImage(img)  # Return the image as a response


@app.route(
    "/image/rgba/<r>/<g>/<b>/<a>/<w>/<h>"
)  # Decorator to define the route for generating an image with RGBA color
def imageRgba(
    r, g, b, a, w, h
):  # Define the imageRgba function that takes the RGBA values and dimensions as arguments
    rgba = (
        int(r),
        int(g),
        int(b),
        float(a),
    )  # Convert the RGB values to integers and the alpha value to a float
    img = Image.new(
        "RGBA", (int(w), int(h)), rgba
    )  # Create a new RGBA image with the specified dimensions and color
    return serveImage(img)  # Return the image as a response


@app.route(
    "/image/random/<w>/<h>"
)  # Decorator to define the route for generating an image with random color
def imageRandom(w, h):
    hexCode = generateRandomHex()
    rgb = HexConverter.hexToRgb(hexCode)
    img = Image.new("RGB", (int(w), int(h)), rgb)
    return serveImage(img)


@app.route(
    "/image/random/tailwind/<w>/<h>"
)  # Decorator to define the route for generating an image with random tailwind color
def imageRandomTailwind(
    w,
    h,
):  # Define the imageRandomTailwind function
    tones = [
        "50",
        "100",
        "200",
        "300",
        "400",
        "500",
        "600",
        "700",
        "800",
        "900",
        "950",
    ]  # Define the list of tones
    file = open("colors/tailwind.json", "r")  # Open the tailwind.json file in read mode
    colors = loads(file.read())  # Read the contents of the file and parse it as JSON
    randomColor = choice(
        list(colors.keys())
    )  # Select a random color from the list of tailwind colors
    hexCode = colors[randomColor][choice(tones)]  # Select a random tone for the color
    rgb = HexConverter.hexToRgb(hexCode)  # Convert the hex code to RGB values
    img = Image.new(
        "RGB", (int(w), int(h)), rgb
    )  # Create a new RGB image with the specified dimensions and color
    return serveImage(img)  # Return the image as a response


@app.route(
    "/image/random/tailwind/tone/<tone>/<w>/<h>"
)  # Decorator to define the route for generating an image with random tailwind color
def imageRandomTailwindSettedTone(
    tone,
    w,
    h,
):  # Define the imageRandomTailwindSettedTone function
    file = open("colors/tailwind.json", "r")  # Open the tailwind.json file in read mode
    colors = loads(file.read())  # Read the contents of the file and parse it as JSON
    randomColor = choice(
        list(colors.keys())
    )  # Select a random color from the list of tailwind colors
    hexCode = colors[randomColor][tone]  # Select a random tone for the color
    rgb = HexConverter.hexToRgb(hexCode)  # Convert the hex code to RGB values
    img = Image.new(
        "RGB", (int(w), int(h)), rgb
    )  # Create a new RGB image with the specified dimensions and color
    return serveImage(img)  # Return the image as a response


@app.route(
    "/image/hex/gradient/<color1>/<color2>/<w>/<h>"
)  # Decorator to define the route for generating a gradient image
def gradientHex(
    color1, color2, w, h
):  # Define the gradientHex function that takes the hex codes of two colors and dimensions as arguments
    rgb1 = HexConverter.hexToRgb(color1)  # Convert the first hex code to RGB values
    rgb2 = HexConverter.hexToRgb(color2)  # Convert the second hex code to RGB values
    img = Image.new(
        "RGB", (int(w), int(h))
    )  # Create a new RGB image with the specified dimensions
    for x in range(int(w)):  # Iterate over the width of the image
        for y in range(int(h)):  # Iterate over the height of the image
            r = int(
                rgb1[0] + (rgb2[0] - rgb1[0]) * x / int(w)
            )  # Calculate the red value based on the gradient
            g = int(
                rgb1[1] + (rgb2[1] - rgb1[1]) * x / int(w)
            )  # Calculate the green value based on the gradient
            b = int(
                rgb1[2] + (rgb2[2] - rgb1[2]) * x / int(w)
            )  # Calculate the blue value based on the gradient
            img.putpixel((x, y), (r, g, b))  # Set the pixel color in the image
    return serveImage(img)  # Return the image as a response


@app.route(
    "/image/random/gradients/<w>/<h>"
)  # Decorator to define the route for generating a random gradient image
def randomGradient(
    w, h
):  # Define the randomGradient function that takes the dimensions as arguments
    hexCode1 = generateRandomHex()  # Generate a random hex code for the first color
    hexCode2 = generateRandomHex()  # Generate a random hex code for the second color
    rgb1 = HexConverter.hexToRgb(hexCode1)  # Convert the first hex code to RGB values
    rgb2 = HexConverter.hexToRgb(hexCode2)  # Convert the second hex code to RGB values
    img = Image.new(
        "RGB", (int(w), int(h))
    )  # Create a new RGB image with the specified dimensions
    for x in range(int(w)):  # Iterate over the width of the image
        for y in range(int(h)):  # Iterate over the height of the image
            r = int(
                rgb1[0] + (rgb2[0] - rgb1[0]) * x / int(w)
            )  # Calculate the red value based on the gradient
            g = int(
                rgb1[1] + (rgb2[1] - rgb1[1]) * x / int(w)
            )  # Calculate the green value based on the gradient
            b = int(
                rgb1[2] + (rgb2[2] - rgb1[2]) * x / int(w)
            )  # Calculate the blue value based on the gradient
            img.putpixel((x, y), (r, g, b))  # Set the pixel color in the image
    return serveImage(img)  # Return the image as a response


@app.route(
    "/image/random/tailwind/gradient/<tone>/<w>/<h>"
)  # Decorator to define the route for generating a random tailwind gradient image
def randomTailwindGradient(
    tone, w, h
):  # Define the randomTailwindGradient function that takes the tone and dimensions as arguments
    file = open("colors/tailwind.json", "r")  # Open the tailwind.json file in read mode
    colors = loads(file.read())  # Read the contents of the file and parse it as JSON
    randomColor1 = choice(
        list(colors.keys())
    )  # Select a random color from the list of tailwind colors
    randomColor2 = choice(
        list(colors.keys())
    )  # Select a random color from the list of tailwind colors
    hexCode1 = colors[randomColor1][tone]  # Select a random tone for the first color
    hexCode2 = colors[randomColor2][tone]  # Select a random tone for the second color
    rgb1 = HexConverter.hexToRgb(hexCode1)  # Convert the first hex code to RGB values
    rgb2 = HexConverter.hexToRgb(hexCode2)  # Convert the second hex code to RGB values
    img = Image.new(
        "RGB", (int(w), int(h))
    )  # Create a new RGB image with the specified dimensions
    for x in range(int(w)):  # Iterate over the width of the image
        for y in range(int(h)):  # Iterate over the height of the image
            r = int(
                rgb1[0] + (rgb2[0] - rgb1[0]) * x / int(w)
            )  # Calculate the red value based on the gradient
            g = int(
                rgb1[1] + (rgb2[1] - rgb1[1]) * x / int(w)
            )  # Calculate the green value based on the gradient
            b = int(
                rgb1[2] + (rgb2[2] - rgb1[2]) * x / int(w)
            )  # Calculate the blue value based on the gradient
            img.putpixel((x, y), (r, g, b))  # Set the pixel color in the image
    return serveImage(img)  # Return the image as a response


if __name__ == "__main__":  # Check if the script is executed directly
    app.run(
        debug=True
    )  # Run the Flask application in debug mode if the script is executed directly
