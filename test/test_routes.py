import unittest
import json
from app.routes import app, cities, countries

class TestCountriesEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_countries(self):
        response = self.app.get('/countries')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), len(countries))

    def test_get_country(self):
        response = self.app.get('/countries/US')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['code'], 'US')

    def test_get_country_not_found(self):
        response = self.app.get('/countries/XX')
        self.assertEqual(response.status_code, 404)

    # Add more tests as needed for country endpoints

class TestCitiesEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_cities(self):
        response = self.app.get('/cities')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    def test_create_city(self):
        new_city = {
            'name': 'New City',
            'country_code': 'US'
            # Add more fields as needed
        }
        response = self.app.post('/cities', data=json.dumps(new_city), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn('id', data)
        self.assertEqual(data['country_code'], 'US')

    # Add more tests as needed for city endpoints

if __name__ == '__main__':
    unittest.main()
