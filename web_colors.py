"""
Basic and extended color list from https://en.wikipedia.org/wiki/Web_colors

The keys of the dictionaries are the web name of the colors, and the values are its hexadecimal RGB
values and a boolean for if it's a purple color.

The purple flag was not defined automatically by code, but manually and visually by the author of
this file.

For extracting the R, G, and B channels of the hexadecimal color, here's a snippet:
from PIL import ImageColor
r, g, b = ImageColor.getcolor('#FF69B4', 'RGB') # r = 255, g = 105, b = 180
"""

basic_colors = {
    'White': '#FFFFFF',
    'Silver': '#C0C0C0',
    'Gray': '#808080',
    'Black': '#000000',
    'Red': '#FF0000',
    'Maroon': '#800000',
    'Yellow': '#FFFF00',
    'Olive': '#808000',
    'Lime': '#00FF00',
    'Green': '#008000',
    'Aqua': '#00FFFF',
    'Teal': '#008080',
    'Blue': '#0000FF',
    'Navy': '#000080',
    'Fuchsia': '#FF00FF',
    'Purple': '#800080',
}

extended_colors = {
    # Pink colors
    'MediumVioletRed': '#C71585',
    'DeepPink': '#FF1493',
    'PaleVioletRed': '#DB7093',
    'HotPink': '#FF69B4',
    'LightPink': '#FFB6C1',
    'Pink': '#FFC0CB',

    # Red colors
    'DarkRed': '#8B0000',
    'Red': '#FF0000',
    'Firebrick': '#B22222',
    'Crimson': '#DC143C',
    'IndianRed': '#CD5C5C',
    'LightCoral': '#F08080',
    'Salmon': '#FA8072',
    'DarkSalmon': '#E9967A',
    'LightSalmon': '#FFA07A',

    # Orange colors
    'OrangeRed': '#FF4500',
    'Tomato': '#FF6347',
    'DarkOrange': '#FF8C00',
    'Coral': '#FF7F50',
    'Orange': '#FFA500',

    # Yellow colors
    'DarkKhaki': '#BDB76B',
    'Gold': '#FFD700',
    'Khaki': '#F0E68C',
    'PeachPuff': '#FFDAB9',
    'Yellow': '#FFFF00',
    'PaleGoldenrod': '#EEE8AA',
    'Moccasin': '#FFE4B5',
    'PapayaWhip': '#FFEFD5',
    'LightGoldenrodYellow': '#FAFAD2',
    'LemonChiffon': '#FFFACD',
    'LightYellow': '#FFFFE0',

    # Brown colors
    'Maroon': '#800000',
    'Brown': '#A52A2A',
    'SaddleBrown': '#8B4513',
    'Sienna': '#A0522D',
    'Chocolate': '#D2691E',
    'DarkGoldenrod': '#B8860B',
    'Peru': '#CD853F',
    'RosyBrown': '#BC8F8F',
    'Goldenrod': '#DAA520',
    'SandyBrown': '#F4A460',
    'Tan': '#D2B48C',
    'Burlywood': '#DEB887',
    'Wheat': '#F5DEB3',
    'NavajoWhite': '#FFDEAD',
    'Bisque': '#FFE4C4',
    'BlanchedAlmond': '#FFEBCD',
    'Cornsilk': '#FFF8DC',

    # Purple, violet, and magenta colors
    'Indigo': '#4B0082',
    'Purple': '#800080',
    'DarkMagenta': '#8B008B',
    'DarkViolet': '#9400D3',
    'DarkSlateBlue': '#483D8B',
    'BlueViolet': '#8A2BE2',
    'DarkOrchid': '#9932CC',
    'Fuchsia': '#FF00FF',
    'Magenta': '#FF00FF',
    'SlateBlue': '#6A5ACD',
    'MediumSlateBlue': '#7B68EE',
    'MediumOrchid': '#BA55D3',
    'MediumPurple': '#9370DB',
    'Orchid': '#DA70D6',
    'Violet': '#EE82EE',
    'Plum': '#DDA0DD',
    'Thistle': '#D8BFD8',
    'Lavender': '#E6E6FA',

    # Blue colors
    'MidnightBlue': '#191970',
    'Navy': '#000080',
    'DarkBlue': '#00008B',
    'MediumBlue': '#0000CD',
    'Blue': '#0000FF',
    'RoyalBlue': '#4169E1',
    'SteelBlue': '#4682B4',
    'DodgerBlue': '#1E90FF',
    'DeepSkyBlue': '#00BFFF',
    'CornflowerBlue': '#6495ED',
    'SkyBlue': '#87CEEB',
    'LightSkyBlue': '#87CEFA',
    'LightSteelBlue': '#B0C4DE',
    'LightBlue': '#ADD8E6',
    'PowderBlue': '#B0E0E6',

    # Cyan colors
    'Teal': '#008080',
    'DarkCyan': '#008B8B',
    'LightSeaGreen': '#20B2AA',
    'CadetBlue': '#5F9EA0',
    'DarkTurquoise': '#00CED1',
    'MediumTurquoise': '#48D1CC',
    'Turquoise': '#40E0D0',
    'Aqua': '#00FFFF',
    'Cyan': '#00FFFF',
    'Aquamarine': '#7FFFD4',
    'PaleTurquoise': '#AFEEEE',
    'LightCyan': '#E0FFFF',

    # Green colors
    'DarkGreen': '#006400',
    'Green': '#008000',
    'DarkOliveGreen': '#556B2F',
    'ForestGreen': '#228B22',
    'SeaGreen': '#2E8B57',
    'Olive': '#808000',
    'OliveDrab': '#6B8E23',
    'MediumSeaGreen': '#3CB371',
    'LimeGreen': '#32CD32',
    'Lime': '#00FF00',
    'SpringGreen': '#00FF7F',
    'MediumSpringGreen': '#00FA9A',
    'DarkSeaGreen': '#8FBC8F',
    'MediumAquamarine': '#66CDAA',
    'YellowGreen': '#9ACD32',
    'LawnGreen': '#7CFC00',
    'Chartreuse': '#7FFF00',
    'LightGreen': '#90EE90',
    'GreenYellow': '#ADFF2F',
    'PaleGreen': '#98FB98',

    # White colors
    'MistyRose': '#FFE4E1',
    'AntiqueWhite': '#FAEBD7',
    'Linen': '#FAF0E6',
    'Beige': '#F5F5DC',
    'WhiteSmoke': '#F5F5F5',
    'LavenderBlush': '#FFF0F5',
    'OldLace': '#FDF5E6',
    'AliceBlue': '#F0F8FF',
    'Seashell': '#FFF5EE',
    'GhostWhite': '#F8F8FF',
    'Honeydew': '#F0FFF0',
    'FloralWhite': '#FFFAF0',
    'Azure': '#F0FFFF',
    'MintCream': '#F5FFFA',
    'Snow': '#FFFAFA',
    'Ivory': '#FFFFF0',
    'White': '#FFFFFF',

    # Gray and black colors
    'Black': '#000000',
    'DarkSlateGray': '#2F4F4F',
    'DimGray': '#696969',
    'SlateGray': '#708090',
    'Gray': '#808080',
    'LightSlateGray': '#778899',
    'DarkGray': '#A9A9A9',
    'Silver': '#C0C0C0',
    'LightGray': '#D3D3D3',
    'Gainsboro': '#DCDCDC',
}
