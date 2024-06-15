import unittest
from datetime import datetime
from app import place, user, Amenity

class TestPlace(unittest.TestCase):

    def setUp(self):
        # Création d'une instance de User pour les tests
        self.host = User("john.doe@example.com", "John", "Doe")

        # Création d'une instance de Place pour les tests
        self.place = Place("Cozy Apartment", "Paris, France", self.host)

    def test_place_initialization(self):
        self.assertIsInstance(self.place.id, str)
        self.assertEqual(self.place.name, "Cozy Apartment")
        self.assertEqual(self.place.location, "Paris, France")
        self.assertEqual(self.place.host, self.host)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)
        self.assertEqual(self.place.amenities, [])
        self.assertEqual(self.place.reviews, [])

    def test_add_amenity(self):
        amenity1 = Amenity("Wi-Fi")
        amenity2 = Amenity("Parking")

        self.assertTrue(self.place.add_amenity(amenity1))
        self.assertIn(amenity1, self.place.amenities)

        # Ajout du même amenity devrait retourner False
        self.assertFalse(self.place.add_amenity(amenity1))

        self.assertTrue(self.place.add_amenity(amenity2))
        self.assertIn(amenity2, self.place.amenities)

    def test_add_review(self):
        review1 = "Great place to stay!"
        review2 = "Nice location and clean."

        self.place.add_review(review1)
        self.assertIn(review1, self.place.reviews)

        self.place.add_review(review2)
        self.assertIn(review2, self.place.reviews)

    def test_str_representation(self):
        expected_str = f'Place({self.place.id}, Cozy Apartment, Paris, France, {self.host})'
        self.assertEqual(str(self.place), expected_str)

if __name__ == '__main__':
    unittest.main()
