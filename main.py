from color_pair_tests import test_number_to_pair, test_pair_to_number

def main():
    # Run test cases for color pair conversions
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    print('Done :)')

if __name__ == '__main__':
    main()
