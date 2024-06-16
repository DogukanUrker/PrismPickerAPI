class HexConverter:
    @staticmethod
    def hexToRgb(hexCode):
        # Remove the '#' character from the hex code
        hexCode = hexCode.lstrip('#')
        
        # Convert the hex code to RGB values
        # by splitting it into three parts (red, green, blue)
        # and converting each part from hexadecimal to decimal
        rgb = tuple(int(hexCode[i:i+2], 16) for i in (0, 2, 4))
        
        # Return the RGB values as a tuple
        return rgb

    @staticmethod
    def hexToRgba(hexCode, alpha):
        # Convert the hex code to RGB values
        rgb = HexConverter.hexToRgb(hexCode)
        
        # Create a new tuple by adding the alpha value to the RGB values
        rgba = rgb + (alpha,)
        
        # Return the RGBA values as a tuple
        return rgba


class RGBConverter:
    @staticmethod
    def rgbToHex(rgb):
        # Convert the RGB values to a hex code
        # by formatting the values as hexadecimal strings
        # and concatenating them with the '#' character
        hexCode = '#{:02x}{:02x}{:02x}'.format(*rgb)
        
        # Return the hex code
        return hexCode

    @staticmethod
    def rgbToRgba(rgb, alpha):
        # Create a new tuple by adding the alpha value to the RGB values
        rgba = rgb + (alpha,)
        
        # Return the RGBA values as a tuple
        return rgba


class RGBAConverter:
    @staticmethod
    def rgbaToRgb(rgba):
        # Extract the RGB values from the RGBA values
        rgb = rgba[:3]
        
        # Return the RGB values as a tuple
        return rgb

    @staticmethod
    def rgbaToHex(rgba):
        # Convert the RGBA values to RGB values
        rgb = RGBAConverter.rgbaToRgb(rgba)
        
        # Convert the RGB values to a hex code
        hexCode = RGBConverter.rgbToHex(rgb)
        
        # Return the hex code
        return hexCode


# Test the converters with some example values and print the results to the console.
print(HexConverter.hexToRgb('#ff0000')) # (255, 0, 0)
print(HexConverter.hexToRgba('#ff0000', 0.5)) # (255, 0, 0, 0.5)

print(RGBConverter.rgbToHex((255, 0, 0))) # #ff0000
print(RGBConverter.rgbToRgba((255, 0, 0), 0.5)) # (255, 0, 0, 0.5)

print(RGBAConverter.rgbaToRgb((255, 0, 0, 0.5))) # (255, 0, 0)
print(RGBAConverter.rgbaToHex((255, 0, 0, 0.5))) # #ff0000
