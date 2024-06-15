import unittest
from datetime import datetime
from app import Country, City  # Assurez-vous d'importer correctement vos classes Country et City

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country = Country("France")  # Créez une instance de Country pour les tests

    def test_country_initialization(self):
        self.assertIsInstance(self.country.id, str)
        self.assertEqual(self.country.name, "France")
        self.assertIsInstance(self.country.created_at, datetime)
        self.assertIsInstance(self.country.updated_at, datetime)
        self.assertEqual(self.country.cities, [])

    def test_add_city(self):
        city1 = City("Paris", self.country)
        city2 = City("Marseille", self.country)
        
        self.country.add_city(city1)
        self.assertIn(city1, self.country.cities)
        self.assertNotIn(city2, self.country.cities)

        self.country.add_city(city2)
        self.assertIn(city2, self.country.cities)

    def test_str_representation(self):
        expected_str = f'Country({self.country.id}, France)'
        self.assertEqual(str(self.country), expected_str)

if __name__ == '__main__':
    unittest.main()
