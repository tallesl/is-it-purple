"""
This script uses the tkcolorpicker library to ask the user for a color and then verifies if the
given color is purple through arbitrary thresholds in the HSV color space.
"""
from tkinter import messagebox
from colorsys import rgb_to_hsv
from tkcolorpicker import askcolor  # type: ignore

PURPLE_MAX_HUE = 0.88
PURPLE_MIN_HUE = 0.78

PURPLE_MIN_SATURATION = 0.2
PURPLE_MIN_BRIGHTNESS = 0.2


def is_purple(r: float, g: float, b: float) -> bool:
    """
    Verifies through the HSV color space if the given RGB color is purple.
    """
    hue, saturation, brightness = rgb_to_hsv(r / 255, g / 255, b / 255)

    valid_hue = PURPLE_MAX_HUE > hue > PURPLE_MIN_HUE
    valid_saturation = saturation > PURPLE_MIN_SATURATION
    valid_brightness = brightness > PURPLE_MIN_BRIGHTNESS

    return valid_hue and valid_saturation and valid_brightness


if __name__ == '__main__':
    while True:
        rgb, _ = askcolor('purple')

        if rgb is None:
            break

        print(is_purple(*rgb))
        messagebox.showinfo(
            'Purple?',
            'Yes, it\'s purple' if is_purple(*rgb) else
            'No, it\'s not purple')
