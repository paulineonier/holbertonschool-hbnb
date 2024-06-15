import unittest
from datetime import datetime
from unittest.mock import MagicMock
from app import city, country

class TestCity(unittest.TestCase):

    def setUp(self):
        self.country = Country("France")  # Créez un exemple de pays pour les tests
        self.city = City("Paris", self.country)  # Créez une instance de City pour les tests

    def test_city_initialization(self):
        self.assertEqual(self.city.name, "Paris")
        self.assertEqual(self.city.country, self.country)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)
        self.assertEqual(self.city.places, [])

    def test_add_place(self):
        place_mock = MagicMock()
        self.city.add_place(place_mock)
        self.assertIn(place_mock, self.city.places)

    def test_add_duplicate_place(self):
        place_mock = MagicMock()
        self.city.add_place(place_mock)
        self.city.add_place(place_mock)
        self.assertEqual(len(self.city.places), 1)

    def test_str_representation(self):
        expected_str = f'City({self.city.id}, Paris, {self.country})'
        self.assertEqual(str(self.city), expected_str)

    def test_invalid_country_type(self):
        with self.assertRaises(ValueError):
            City("Berlin", "Germany")

if __name__ == '__main__':
    unittest.main()
