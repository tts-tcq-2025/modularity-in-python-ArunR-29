from color_pair_utils import color_pair_from_number, pair_number_from_color_pair

def test_number_to_pair(pair_number, expected_major_color, expected_minor_color):
    """
    Test conversion from pair number to color pair.
    :param pair_number: The input pair number to test.
    :param expected_major_color: The expected major color for the pair.
    :param expected_minor_color: The expected minor color for the pair.
    """
    # major_color: Resulting major color from conversion
    # minor_color: Resulting minor color from conversion
    major_color, minor_color = color_pair_from_number(pair_number)
    assert major_color == expected_major_color
    assert minor_color == expected_minor_color

def test_pair_to_number(major_color, minor_color, expected_pair_number):
    """
    Test conversion from color pair to pair number.
    :param major_color: The major color to test.
    :param minor_color: The minor color to test.
    :param expected_pair_number: The expected pair number for the color pair.
    """
    # pair_number: Resulting pair number from conversion
    pair_number = pair_number_from_color_pair(major_color, minor_color)
    assert pair_number == expected_pair_number
