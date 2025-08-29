from color_constants import MAJOR_COLORS, MINOR_COLORS

def color_pair_to_string(major_color, minor_color):
    """Return a string representation of a color pair."""
    return f'{major_color} {minor_color}'

def color_pair_from_number(pair_number):
    """
    Given a pair number, return the corresponding major and minor colors.
    Raises Exception if indices are out of range.
    """
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    if major_index >= len(MAJOR_COLORS):
        raise Exception('Major index out of range')
    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def pair_number_from_color_pair(major_color, minor_color):
    """
    Given major and minor colors, return the corresponding pair number.
    Raises Exception if colors are not found.
    """
    try:
        major_index = MAJOR_COLORS.index(major_color)
    except ValueError:
        raise Exception('Major index out of range')
    try:
        minor_index = MINOR_COLORS.index(minor_color)
    except ValueError:
        raise Exception('Minor index out of range')
    return major_index * len(MINOR_COLORS) + minor_index + 1
