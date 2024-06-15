from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from datetime import datetime
from uuid import uuid4

app = Flask(__name__)
api = Api(app)

# Pre-loaded country data
countries = [
    {'code': 'US', 'name': 'United States'},
    {'code': 'CA', 'name': 'Canada'},
    {'code': 'FR', 'name': 'France'},
    # Add more countries as needed
]

# Simulated storage for cities
cities = []

class CountryList(Resource):
    def get(self):
        return jsonify(countries)

class Country(Resource):
    def get(self, country_code):
        country = next((c for c in countries if c['code'] == country_code), None)
        if country:
            return jsonify(country)
        return {'message': 'Country not found'}, 404

class CityList(Resource):
    def get(self):
        return jsonify(cities)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='City name is required')
        parser.add_argument('country_code', type=str, required=True, help='Country code is required')
        # Add more fields as needed
        args = parser.parse_args()

        # Validate country_code
        if args['country_code'] not in [c['code'] for c in countries]:
            return {'message': 'Invalid country code'}, 400

        # Validate uniqueness of city name within the same country
        for city in cities:
            if city['name'] == args['name'] and city['country_code'] == args['country_code']:
                return {'message': 'City name already exists in the country'}, 409

        # Create new city
        city = {
            'id': str(uuid4()),
            'name': args['name'],
            'country_code': args['country_code'],
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow()
        }
        cities.append(city)
        return city, 201

class City(Resource):
    def get(self, city_id):
        city = next((c for c in cities if c['id'] == city_id), None)
        if city:
            return jsonify(city)
        return {'message': 'City not found'}, 404

    def put(self, city_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('country_code', type=str)
        # Add more fields as needed
        args = parser.parse_args()

        city = next((c for c in cities if c['id'] == city_id), None)
        if not city:
            return {'message': 'City not found'}, 404

        # Update city data
        if args['name']:
            city['name'] = args['name']
        if args['country_code']:
            # Validate country_code
            if args['country_code'] not in [c['code'] for c in countries]:
                return {'message': 'Invalid country code'}, 400
            city['country_code'] = args['country_code']
        city['updated_at'] = datetime.utcnow()
        return city, 200

    def delete(self, city_id):
        global cities
        cities = [c for c in cities if c['id'] != city_id]
        return '', 204

# Endpoint routes
api.add_resource(CountryList, '/countries')
api.add_resource(Country, '/countries/<string:country_code>')
api.add_resource(CityList, '/cities')
api.add_resource(City, '/cities/<string:city_id>')

if __name__ == '__main__':
    app.run(debug=True)
