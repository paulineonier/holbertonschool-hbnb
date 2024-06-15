import unittest
from datetime import datetime
from app import Amenity  

class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity("WiFi")  # Créez une instance de Amenity pour les tests

    def test_amenity_initialization(self):
        self.assertIsInstance(self.amenity.id, str)
        self.assertEqual(self.amenity.name, "WiFi")
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_str_representation(self):
        expected_str = f'Amenity({self.amenity.id}, WiFi)'
        self.assertEqual(str(self.amenity), expected_str)

if __name__ == '__main__':
    unittest.main()
