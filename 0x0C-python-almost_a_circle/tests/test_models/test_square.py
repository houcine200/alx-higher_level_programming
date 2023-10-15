import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_size_property(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        square.size = 10
        self.assertEqual(square.size, 10)

    def test_str_method(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_update_method(self):
        square = Square(5, 2, 3, 1)
        square.update(2, 4, 6, 8)
        self.assertEqual(str(square), "[Square] (2) 6/8 - 4")

    def test_to_dictionary_method(self):
        square = Square(5, 2, 3, 1)
        square_dict = square.to_dictionary()
        expected_dict = {
            'id': 1,
            'size': 5,
            'x': 2,
            'y': 3
        }
        self.assertDictEqual(square_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
