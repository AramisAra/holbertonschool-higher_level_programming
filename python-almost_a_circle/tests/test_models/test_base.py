import unittest
import pep8
from models.base import Base

class TestBase(unittest.TestCase):
    def test_pep8_conformance(self):
        """Test that all modules conform to PEP8."""
        pep8style = pep8.StyleGuide()
        result = pep8style.check_files(['models'])
        self.assertEqual(result.total_errors, 0, "PEP8 style violations found")

    def test_base_init(self):
        """Test the initialization of the Base class."""
        base = Base()
        self.assertEqual(base.id, 1)

    def test_base_init_with_id(self):
        """Test the initialization of the Base class with a specific id."""
        base = Base(5)
        self.assertEqual(base.id, 5)

    def test_to_json_string(self):
        """Test the to_json_string method of the Base class."""
        list_dictionaries = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        json_string = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_string, '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]')

    def test_save_to_file(self):
        """Test the save_to_file method of the Base class."""
        list_objs = [Base(1), Base(2)]
        Base.save_to_file(list_objs)
        # Check if the file was created and contains the correct data

    def test_from_json_string(self):
        """Test the from_json_string method of the Base class."""
        json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        list_dictionaries = Base.from_json_string(json_string)
        self.assertEqual(list_dictionaries, [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}])

    def test_create(self):
        """Test the create method of the Base class."""
        dictionary = {'id': 1, 'name': 'John'}
        obj = Base.create(**dictionary)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.name, 'John')

    def test_load_from_file(self):
        """Test the load_from_file method of the Base class."""
        # Create a JSON file with some data
        list_objs = [Base(1), Base(2)]
        Base.save_to_file(list_objs)
        # Call load_from_file and check if the objects were loaded correctly

if __name__ == '__main__':
    unittest.main()