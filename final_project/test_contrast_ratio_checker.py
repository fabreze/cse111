import pytest
from contrast_ratio_checker import read_css_file, calculate_contrast_ratio, calculate_relative_luminance, parse_rgb, hex_to_rgb, expand_hex_color, srgb_to_linear

def test_read_css_file():

    css_dictionary = read_css_file('C:\\GitHub\\cse111\\final_project\\styles.css')

    # Verify that the read_css function returns a dictionary.
    assert isinstance(css_dictionary, dict), \
        "read_css_file function must return a dictionary: " \
        f" expected a dictionary but found a {type(css_dictionary)}"
    
    assert read_css_file('non_existent_file.css') == None
    assert read_css_file('C:\\GitHub\\cse111\\final_project\\large_styles.css') == {'body': {'text_color': '#000000', 'text_color_type': 'hexcode', 'background_color': '#ffffff', 'background_color_type': 'hexcode'}, '.nav': {'text_color': '#ff0000', 'text_color_type': 'hexcode', 'background_color': '#0000ff', 'background_color_type': 'hexcode'}, '.content': {'text_color': 'rgb(51, 51, 51)', 'text_color_type': 'rgb', 'background_color': 'rgb(255, 255, 255)', 'background_color_type': 'rgb'}, '.transparent-bg': {'text_color': '#000000', 'text_color_type': 'hexcode', 'background_color': 'rgba(255, 255, 255, 0.9)', 'background_color_type': 'unsupported color format'}, '.mixed': {'text_color': '#ffffff', 'text_color_type': 'hexcode', 'background_color': 'rgb(0, 0, 0)', 'background_color_type': 'rgb'}, '.named-colors': {'text_color': 'black', 'text_color_type': 'unsupported color format', 'background_color': 'white', 'background_color_type': 'unsupported color format'}, '.poor-contrast-1': {'text_color': '#777777', 'text_color_type': 'hexcode', 'background_color': '#888888', 'background_color_type': 'hexcode'}, '.poor-contrast-2': {'text_color': 'rgb(170, 170, 170)', 'text_color_type': 'rgb', 'background_color': 'rgb(180, 180, 180)', 'background_color_type': 'rgb'}, '.large-text-ok': {'text_color': '#666666', 'text_color_type': 'hexcode', 'background_color': '#ffffff', 'background_color_type': 'hexcode'}, '.excellent-contrast': {'text_color': '#000000', 'text_color_type': 'hexcode', 'background_color': '#ffff00', 'background_color_type': 'hexcode'}, '.hex-shorthand': {'text_color': '#aabbcc', 'text_color_type': 'hexcode', 'background_color': '#ddeeff', 'background_color_type': 'hexcode'}, '.hex-shorthand-2': {'text_color': '#0099ff', 'text_color_type': 'hexcode', 'background_color': '#ffffff', 'background_color_type': 'hexcode'}, '.uppercase-hex': {'text_color': '#FFFFFF', 'text_color_type': 'hexcode', 'background_color': '#000000', 'background_color_type': 'hexcode'}, '#main-container': {'text_color': '#222222', 'text_color_type': 'hexcode', 'background_color': '#eeeeee', 'background_color_type': 'hexcode'}, '.container > .inner': {'text_color': 'rgb(34, 34, 34)', 'text_color_type': 'rgb', 'background_color': 'rgb(238, 238, 238)', 'background_color_type': 'rgb'}, 'input[type="text"]': {'text_color': '#000000', 'text_color_type': 'hexcode', 'background_color': '#ffffff', 'background_color_type': 'hexcode'}, '.btn, .button, input[type="submit"]': {'text_color': 'white', 'text_color_type': 'unsupported color format', 'background_color': '#007bff', 'background_color_type': 'hexcode'}, '.btn:hover': {'text_color': '#ffffff', 'text_color_type': 'hexcode', 'background_color': '#0056b3', 'background_color_type': 'hexcode'}, '.themed': {'text_color': 'var(--text-color)', 'text_color_type': 'unsupported color format', 'background_color': 'var(--bg-color)', 'background_color_type': 'unsupported color format'}, 'a:link': {'text_color': '#0000ee', 'text_color_type': 'hexcode', 'background_color': 'transparent', 'background_color_type': 'unsupported color format'}, 'a:visited': {'text_color': '#551a8b', 'text_color_type': 'hexcode', 'background_color': 'transparent', 'background_color_type': 'unsupported color format'}, 'h1, h2, h3, h4, h5, h6': {'text_color': '#2c3e50', 'text_color_type': 'hexcode', 'background_color': 'transparent', 'background_color_type': 'unsupported color format'}, 'p': {'text_color': '#34495e', 'text_color_type': 'hexcode', 'background_color': 'inherit', 'background_color_type': 'unsupported color format'}, '.alert-success': {'text_color': '#155724', 'text_color_type': 'hexcode', 'background_color': '#d4edda', 'background_color_type': 'hexcode'}, '.alert-danger': {'text_color': '#721c24', 'text_color_type': 'hexcode', 'background_color': '#f8d7da', 'background_color_type': 'hexcode'}, '.alert-warning': {'text_color': '#856404', 'text_color_type': 'hexcode', 'background_color': '#fff3cd', 'background_color_type': 'hexcode'}, '.alert-info': {'text_color': '#0c5460', 'text_color_type': 'hexcode', 'background_color': '#d1ecf1', 'background_color_type': 'hexcode'}, '.current-color-example': {'text_color': '#333333', 'text_color_type': 'hexcode', 'background_color': '#ffffff', 'background_color_type': 'hexcode'}, '.inherit-example': {'text_color': 'inherit', 'text_color_type': 'unsupported color format', 'background_color': 'inherit', 'background_color_type': 'unsupported color format'}, '.hsl-colors': {'text_color': 'hsl(0, 100%, 50%)', 'text_color_type': 'unsupported color format', 'background_color': 'hsl(120, 100%, 50%)', 'background_color_type': 'unsupported color format'}, '.hsla-colors': {'text_color': 'hsla(240, 100%, 50%, 0.7)', 'text_color_type': 'unsupported color format', 'background_color': 'hsla(60, 100%, 50%, 0.5)', 'background_color_type': 'unsupported color format'}, '.system-colors': {'text_color': 'ButtonText', 'text_color_type': 'unsupported color format', 'background_color': 'ButtonFace', 'background_color_type': 'unsupported color format'}, '.new-colors': {'text_color': 'rebeccapurple', 'text_color_type': 'unsupported color format', 'background_color': 'transparent', 'background_color_type': 'unsupported color format'}, '.similar-1': {'text_color': '#fefefe', 'text_color_type': 'hexcode', 'background_color': '#ffffff', 'background_color_type': 'hexcode'}, '.similar-2': {'text_color': '#010101', 'text_color_type': 'hexcode', 'background_color': '#000000', 'background_color_type': 'hexcode'}, '.max-contrast': {'text_color': '#000000', 'text_color_type': 'hexcode', 'background_color': '#ffffff', 'background_color_type': 'hexcode'}, '.min-contrast': {'text_color': '#aaaaaa', 'text_color_type': 'hexcode', 'background_color': '#bbbbbb', 'background_color_type': 'hexcode'}, '.accessible-1': {'text_color': '#005a9c', 'text_color_type': 'hexcode', 'background_color': '#ffffff', 'background_color_type': 'hexcode'}, '.accessible-2': {'text_color': '#ffffff', 'text_color_type': 'hexcode', 'background_color': '#005a9c', 'background_color_type': 'hexcode'}, '.accessible-3': {'text_color': '#d04437', 'text_color_type': 'hexcode', 'background_color': '#fce8e6', 'background_color_type': 'hexcode'}, '.cb-friendly-1': {'text_color': '#006400', 'text_color_type': 'hexcode', 'background_color': '#f5f5f5', 'background_color_type': 'hexcode'}, '.cb-friendly-2': {'text_color': '#8b4513', 'text_color_type': 'hexcode', 'background_color': '#fffacd', 'background_color_type': 'hexcode'}, '.dark-mode': {'text_color': '#e0e0e0', 'text_color_type': 'hexcode', 'background_color': '#121212', 'background_color_type': 'hexcode'}, '.dark-mode-card': {'text_color': '#ffffff', 'text_color_type': 'hexcode', 'background_color': '#1e1e1e', 'background_color_type': 'hexcode'}, '.animated': {'text_color': '#000000', 'text_color_type': 'hexcode', 'background_color': '#ffffff', 'background_color_type': 'hexcode'}, '.complex-selector': {'text_color': '#123456', 'text_color_type': 'hexcode', 'background_color': '#abcdef', 'background_color_type': 'hexcode'}, '.important-styles': {'text_color': 'red', 'text_color_type': 'unsupported color format', 'background_color': 'yellow', 'background_color_type': 'unsupported color format'}, '.unicode-✓': {'text_color': '#000000', 'text_color_type': 'hexcode', 'background_color': '#ffffff', 'background_color_type': 'hexcode'}, 'div.container > section.main > article.post > header > h1.title': {'text_color': '#2c3e50', 'text_color_type': 'hexcode', 'background_color': '#ecf0f1', 'background_color_type': 'hexcode'}, '[data-theme="dark"]': {'text_color': '#ffffff', 'text_color_type': 'hexcode', 'background_color': '#000000', 'background_color_type': 'hexcode'}, '.modal-overlay': {'text_color': '#333333', 'text_color_type': 'hexcode', 'background_color': 'rgba(0, 0, 0, 0.5)', 'background_color_type': 'unsupported color format'}, '.modal-content': {'text_color': '#2c3e50', 'text_color_type': 'hexcode', 'background_color': '#ffffff', 'background_color_type': 'hexcode'}} 
    assert read_css_file('C:\\GitHub\\cse111\\final_project\\styles.css') == {'body':{'text_color': '#000000', 'text_color_type': 'hexcode', 'background_color': '#FFFFFF', 'background_color_type': 'hexcode'}, 'h1':{'text_color': 'rgb(0, 0, 255)', 'text_color_type': 'rgb', 'background_color': 'rgb(255, 255, 0)', 'background_color_type': 'rgb'}, 'p':{'text_color': '#777777', 'text_color_type': 'hexcode', 'background_color': 'rgb(12, 108, 24)', 'background_color_type': 'rgb'}}

def test_calculate_contrast_ratio():

    contrast_ratio = calculate_contrast_ratio('#000000', '#FFFFFF', 'hexcode', 'hexcode')

    assert isinstance(calculate_contrast_ratio('#000000', '#FFFFFF', 'hexcode', 'hexcode'), float), \
        "calculate_contrast_ratio function must return a float: " \
        f" expected a float but found a {type(contrast_ratio)}"
    
    assert calculate_contrast_ratio('#000000', '#FFFFFF', 'hexcode', 'hexcode') == 21.0
    assert calculate_contrast_ratio('rgb(0, 0, 0)', 'rgb(255, 255, 255)', 'rgb', 'rgb') == 21.0
    assert calculate_contrast_ratio('#777777', 'rgb(12,108,24)', 'hexcode', 'rgb') == pytest.approx(1.48, 0.01)

def test_calculate_relative_luminance():

    luminance = calculate_relative_luminance([0,0,0])

    assert isinstance(calculate_relative_luminance([0, 0, 0]), float), \
        "calculate_relative_luminance function must return a float: " \
        f" expected a float but found a {type(luminance)}"
    
    assert calculate_relative_luminance([0,0,0]) == 0.0
    assert calculate_relative_luminance([255,255,255]) == 1.0
    assert calculate_relative_luminance([12,108,24]) == pytest.approx(0.10869, 0.0001)

def test_parse_rgb():

    rgb = parse_rgb('rgb(12, 108, 24)')

    assert isinstance(parse_rgb('rgb(12, 108, 24)'), list), \
        "parse_rgb function must return a list: " \
        f" expected a list but found a {type(rgb)}"
    
    assert parse_rgb('rgb(0,0,0)') == [0, 0, 0]
    assert parse_rgb('rgb(255, 255, 255)') == [255, 255, 255]
    assert parse_rgb('rgb(12, 108, 24)') == [12, 108, 24]

def test_hex_to_rgb():

    rgb = hex_to_rgb('#000000')

    assert isinstance(hex_to_rgb('#000000'), list), \
        "hex_to_rgb function must return a list: " \
        f" expected a list but found a {type(rgb)}"
    
    assert hex_to_rgb('#000000') == [0, 0, 0]
    assert hex_to_rgb('#FFFFFF') == [255, 255, 255]
    assert hex_to_rgb('#0C6C18') == [12, 108, 24]

def test_expand_hex_color():
    expanded_hex = expand_hex_color('#0C6')

    assert isinstance(expand_hex_color('#0C6'), str), \
        "expand_hex_color function must return a string: " \
        f" expected a string but found a {type(expanded_hex)}"
    
    assert expand_hex_color('#000') == '#000000'
    assert expand_hex_color('#FFF') == '#FFFFFF'
    assert expand_hex_color('#0C6') == '#00CC66'

def test_srgb_to_linear():
    linear_value = srgb_to_linear(0.5)

    assert isinstance(srgb_to_linear(0.5), float), \
        "srgb_to_linear function must return a float: " \
        f" expected a float but found a {type(linear_value)}"
    
    assert srgb_to_linear(0.0) == 0.0
    assert srgb_to_linear(1.0) == 1.0
    assert srgb_to_linear(0.5) == pytest.approx(0.21404, 0.0001)

pytest.main(["-v", "--tb=line", "-rN", __file__])