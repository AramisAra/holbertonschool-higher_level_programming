import unittest
import pep8
from models.rectangle import Rectangle

class TestModels(unittest.TestCase):
    def test_pep8_conformance(self):
        """Test that all modules conform to PEP8."""
        pep8style = pep8.StyleGuide()
        result = pep8style.check_files(['models'])
        self.assertEqual(result.total_errors, 0, "PEP8 style violations found")

    def test_rectangle_init(self):
        """Test the initialization of the Rectangle class."""
        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 1)

    def test_rectangle_area(self):
        """Test the area method of the Rectangle class."""
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

    def test_rectangle_str(self):
        """Test the __str__ method of the Rectangle class."""
        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 2/3 - 5/10")

    def test_rectangle_update(self):
        """Test the update method of the Rectangle class."""
        rectangle = Rectangle(5, 10, 2, 3, 1)
        rectangle.update(2, 7, 8, 4, 5)
        self.assertEqual(rectangle.width, 7)
        self.assertEqual(rectangle.height, 8)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)
        self.assertEqual(rectangle.id, 2)

    def test_rectangle_to_dictionary(self):
        """Test the to_dictionary method of the Rectangle class."""
        rectangle = Rectangle(5, 10, 2, 3, 1)
        dictionary = rectangle.to_dictionary()
        self.assertEqual(dictionary, {'x': 2, 'y': 3, 'id': 1, 'width': 5, 'height': 10})

    # Add more test cases here

if __name__ == '__main__':
    unittest.main()