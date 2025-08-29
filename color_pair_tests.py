from color_pair_utils import color_pair_from_number, pair_number_from_color_pair

def test_number_to_pair(pair_number, expected_major_color, expected_minor_color):
    """Test conversion from pair number to color pair."""
    major_color, minor_color = color_pair_from_number(pair_number)
    assert major_color == expected_major_color
    assert minor_color == expected_minor_color

def test_pair_to_number(major_color, minor_color, expected_pair_number):
    """Test conversion from color pair to pair number."""
    pair_number = pair_number_from_color_pair(major_color, minor_color)
    assert pair_number == expected_pair_number
