import unittest
from datetime import datetime
from app import Review, User, Place

class TestReview(unittest.TestCase):

    def setUp(self):
        # Création d'une instance de User pour les tests
        self.user = User("john.doe@example.com", "John", "Doe")

        # Création d'une instance de Place pour les tests
        self.place = Place("Cozy Apartment", "Paris, France", self.user)

        # Création d'une instance de Review pour les tests
        self.review = Review("Great place to stay!", self.user, self.place)

    def test_review_initialization(self):
        self.assertIsInstance(self.review.id, str)
        self.assertEqual(self.review.content, "Great place to stay!")
        self.assertEqual(self.review.user, self.user)
        self.assertEqual(self.review.place, self.place)
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_str_representation(self):
        expected_str = f'Review({self.review.id}, Great place to stay!, {self.user}, {self.place})'
        self.assertEqual(str(self.review), expected_str)

if __name__ == '__main__':
    unittest.main()
