class HexConverter:  # Class for converting hex codes to RGB and RGBA values
    @staticmethod  # Decorator to define a static method
    def hexToRgb(hexCode):  # Define a static method to convert a hex code to RGB values
        # Remove the '#' character from the hex code
        hexCode = hexCode.lstrip("#")

        # Convert the hex code to RGB values
        # by splitting it into three parts (red, green, blue)
        # and converting each part from hexadecimal to decimal
        rgb = tuple(int(hexCode[i : i + 2], 16) for i in (0, 2, 4))

        # Return the RGB values as a tuple
        return rgb

    @staticmethod  # Decorator to define a static method
    def hexToRgba(
        hexCode, alpha
    ):  # Define a static method to convert a hex code to RGBA values
        # Convert the hex code to RGB values
        rgb = HexConverter.hexToRgb(hexCode)

        # Create a new tuple by adding the alpha value to the RGB values
        rgba = rgb + (alpha,)

        # Return the RGBA values as a tuple
        return rgba


class RGBConverter:  # Class for converting RGB and RGBA values to hex codes
    @staticmethod  # Decorator to define a static method
    def rgbToHex(rgb):  # Define a static method to convert RGB values to a hex code
        # Convert the RGB values to a hex code
        # by formatting the values as hexadecimal strings
        # and concatenating them with the '#' character
        hexCode = "#{:02x}{:02x}{:02x}".format(*rgb)

        # Return the hex code
        return hexCode

    @staticmethod  # Decorator to define a static method
    def rgbToRgba(
        rgb, alpha
    ):  # Define a static method to convert RGB values to RGBA values
        # Create a new tuple by adding the alpha value to the RGB values
        rgba = rgb + (alpha,)

        # Return the RGBA values as a tuple
        return rgba


class RGBAConverter:  # Class for converting RGBA values to RGB values and hex codes
    @staticmethod  # Decorator to define a static method
    def rgbaToRgb(rgba):  # Define a static method to convert RGBA values to RGB values
        # Extract the RGB values from the RGBA values
        rgb = rgba[:3]

        # Return the RGB values as a tuple
        return rgb

    @staticmethod  # Decorator to define a static method
    def rgbaToHex(rgba):  # Define a static method to convert RGBA values to a hex code
        # Convert the RGBA values to RGB values
        rgb = RGBAConverter.rgbaToRgb(rgba)

        # Convert the RGB values to a hex code
        hexCode = RGBConverter.rgbToHex(rgb)

        # Return the hex code
        return hexCode
