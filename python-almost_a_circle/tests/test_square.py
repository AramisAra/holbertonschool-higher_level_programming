import unittest
import pep8
from models.square import Square

class TestModels(unittest.TestCase):
    def test_pep8_conformance(self):
        """Test that all modules conform to PEP8."""
        pep8style = pep8.StyleGuide()
        result = pep8style.check_files(['models'])
        self.assertEqual(result.total_errors, 0, "PEP8 style violations found")

    def test_square_init(self):
        """Test the initialization of the Square class."""
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_square_area(self):
        """Test the area method of the Square class."""
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_square_str(self):
        """Test the __str__ method of the Square class."""
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    # Add more test cases here

if __name__ == '__main__':
    unittest.main()