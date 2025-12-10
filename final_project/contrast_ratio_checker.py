"""
Author: Fabrizio Caballero

"""
import cssutils

def main():
    file_path = 'C:\\GitHub\\cse111\\final_project\\styles.css'
    css_dictionary = read_css_file(file_path)

    print("****************************************************************************************************************\n")
    print(f"Color Contrast Checker for {file_path} using WCAG AA standards")
    print("Supported color formats: hexcode and rgb()\n")
    print("****************************************************************************************************************\n")
    

    for selector in css_dictionary:
        text_color = css_dictionary[selector]['text_color']
        background_color = css_dictionary[selector]['background_color']
        text_color_type = css_dictionary[selector]['text_color_type']
        background_color_type = css_dictionary[selector]['background_color_type']

        contrast_ratio = calculate_contrast_ratio(text_color, background_color, text_color_type, background_color_type)
        
        print(f"Class/Selector: {selector}")
        if contrast_ratio >= 4.5:
            print(f"Small Text - Contrast Ratio: {contrast_ratio:.2f} - PASS")
        else:
            print(f"Small Text - Contrast Ratio: {contrast_ratio:.2f} - FAIL")

        if contrast_ratio >= 3.0:
            print(f"Large Text - Contrast Ratio: {contrast_ratio:.2f} - PASS\n")
        else:
            print(f"Large Text - Contrast Ratio: {contrast_ratio:.2f} - FAIL\n")
        print("----------------------------------------------------------------------------------------------------------------\n")

#If the hexcode is in shorthand format, expand it to full format.
def expand_hex_color(hexcode):
    expanded_hex = ''
    if len(hexcode) == 4:
        for char in (1,2,3):
            expanded_hex += hexcode[char] * 2
        expanded_hex = '#' + expanded_hex
        return expanded_hex
    else:
        return hexcode
        
# Reads a CSS file and creates a dictionary with the selectors as keys and their text and background colors as values.
def read_css_file(file_name):
    try:
        sheet = cssutils.parseFile(file_name)
        css_dictionary = {}
        
        for rule in sheet:
            if rule.type == rule.STYLE_RULE:
                selector = rule.selectorText
                text_color = rule.style.getPropertyValue('color')
                background_color = rule.style.getPropertyValue('background-color')
                text_color_type = ''
                background_color_type = ''

                if text_color and background_color:
                    if 'rgb' in text_color:
                        text_color_type = 'rgb'
                    elif '#' in text_color:
                        text_color_type = 'hexcode'
                        text_color = expand_hex_color(text_color)
                    else:
                        text_color_type = 'unsupported color format'
                    
                    if 'rgb' in background_color:
                        background_color_type = 'rgb'   
                    elif '#' in background_color:
                        background_color_type = 'hexcode'
                        background_color = expand_hex_color(background_color)
                    else:
                        background_color_type = 'unsupported color format'

                    rule_dictionary = {'text_color': text_color, 'text_color_type': text_color_type ,'background_color': background_color, 'background_color_type': background_color_type}
                    css_dictionary[selector] = rule_dictionary

        return css_dictionary

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")

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
def calculate_contrast_ratio(textColor, backgroundColor, textColorType, backgroundColorType):
    rgb1 = []
    rgb2 = []

    if textColorType == 'hexcode':
        rgb1 = hex_to_rgb(textColor)
    elif textColorType == 'rgb':
        rgb1 = parse_rgb(textColor)

    if backgroundColorType == 'hexcode':
        rgb2 = hex_to_rgb(backgroundColor)
    elif backgroundColorType == 'rgb':
        rgb2 = parse_rgb(backgroundColor)

    relative_luminance1 = calculate_relative_luminance(rgb1)
    relative_luminance2 = calculate_relative_luminance(rgb2)

    dark_relative_luminance = 0
    light_relative_luminance = 0

    if(relative_luminance1 <= relative_luminance2):
        dark_relative_luminance = relative_luminance1
        light_relative_luminance = relative_luminance2
    else:
        dark_relative_luminance = relative_luminance2
        light_relative_luminance = relative_luminance1
        

    contrast_ratio = (light_relative_luminance + 0.05) / (dark_relative_luminance + 0.05)
    return contrast_ratio

name = "__main__"
if __name__ == "__main__":
  main()