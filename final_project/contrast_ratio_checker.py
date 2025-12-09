"""
Author: Fabrizio Caballero

"""
import cssutils

def main():
    read_css('styles.css')
    return

def read_css(file_name):
    try:
        with open(file_name, 'r') as css_file:
            css_content = cssutils.parseFile(css_file)
            print(css_content)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    return

#Parses a string into a list representing the rgb values of a color.
def parse_rgb(rgb_string):
    rgb_string = rgb_string.strip('rgb() ')
    rgb_values = rgb_string.split(',')
    rgb = []
    for value in rgb_values:
        rgb.append(int(value))
    return rgb

# Converts hexcode represented in a string, into a list with three values, representing the red, blue, and green values in a color.
def hex_to_rgb(hexcode):
    hexcode = hexcode.strip('#')
    rgb = []
    for i in (0, 2, 4):
        rgb.append(int(hexcode[i:i+2], 16))
    return rgb

# Converts a standard rgb value into linear rgb value.
def srgb_to_linear(rgb_value):
    if rgb_value <= 0.04045:
        return rgb_value / 12.92
    else:
        return ((rgb_value + 0.055) / 1.055) ** 2.4

# Takes in an rgb value saved as a list and gives the relative lumninance of that color.
def calculate_relative_luminance(rgb):
    red = rgb[0]/255
    green = rgb[1]/255
    blue = rgb[2]/255

    red_linear = srgb_to_linear(red)
    green_linear = srgb_to_linear(green)
    blue_linear = srgb_to_linear(blue)

    
    relative_luminance = (0.2126 * red_linear) + (0.7152 * green_linear) + (0.0722 * blue_linear)
    return relative_luminance

# Asks the user for a text color and background color, then calculates the contrast ratio between the two colors.
def calculate_contrast_ratio(textColor, backgroundColor, colorSystem='hexcode'):
    rgb1 = []
    rgb2 = []

    if colorSystem == 'hexcode':
        rgb1 = hex_to_rgb(textColor)
        rgb2 = hex_to_rgb(backgroundColor)
    elif colorSystem == 'rgb':
        rgb1 = parse_rgb(textColor)
        rgb2 = parse_rgb(backgroundColor)

    relative_luminance1 = calculate_relative_luminance(rgb1)
    relative_luminance2 = calculate_relative_luminance(rgb2)

    contrast_ratio = (relative_luminance1 + 0.05) / (relative_luminance2 + 0.05)
    return contrast_ratio

name = "__main__"
if __name__ == "__main__":
  main()