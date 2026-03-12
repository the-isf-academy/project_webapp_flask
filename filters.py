# COLOR FORMATTING HELPERS
from colorsys import rgb_to_hsv, hsv_to_rgb # built-in Python functions


def clamp(value, low, high):
    "Ensures that the value is between low and high"
    return min(max(low, value), high)

def int2hex(int_value):
    "Converts an integer value like 15 to a two-digit hex string like 0b"
    return hex(int_value)[2:].zfill(2)

def rgb_to_hex(color):
    """Returns a hex representation of the color like #00ff00 (green) suitable for CSS.
    """
    return f"#{int2hex(color['red'])}{int2hex(color['green'])}{int2hex(color['blue'])}"

def adjust_hue(color, delta):
    "Adjust the hue of the color by `delta`."
    h, s, v  = rgb_to_hsv(color['red']/255, color['green']/255, color['blue']/255)
    r, g, b = hsv_to_rgb(h + delta % 1, s, v)

    color_dict =  {'red': int(r*255), 'green':int(g*255), 'blue':int(b*255)}
    name = rgb_to_hex(color_dict)
    color_dict['name'] = name

    return color_dict

def adjust_saturation(color, delta):
    "Adjust the saturation of the color by `delta`."
    h, s, v  = rgb_to_hsv(color['red']/255, color['green']/255, color['blue']/255)
    r, g, b = hsv_to_rgb(h, clamp(s + delta, 0, 1), v)

    color_dict =  {'red': int(r*255), 'green':int(g*255), 'blue':int(b*255)}
    name = rgb_to_hex(color_dict)
    color_dict['name'] = name

    return color_dict