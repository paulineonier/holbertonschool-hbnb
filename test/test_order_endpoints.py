import unittest
import json
from app_flask import app  # Importez votre instance d'application Flask

class TestOrderEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_post_order(self):
        # Test de création d'une nouvelle commande
        data = {
            'order_id': 1,
            'product': 'Product A',
            'quantity': 10
        }
        response = self.app.post('/orders', json=data)
        self.assertEqual(response.status_code, 201)

        # Assurez-vous que la commande est bien ajoutée dans le système (vous devrez ajuster ceci selon votre implémentation)
        # Exemple de validation selon la réponse attendue
        order = json.loads(response.data)
        self.assertEqual(order['product'], 'Product A')
        self.assertEqual(order['quantity'], 10)

    def test_get_all_orders(self):
        # Test de récupération de toutes les commandes
        response = self.app.get('/orders')
        self.assertEqual(response.status_code, 200)
        orders = json.loads(response.data)
        self.assertTrue(len(orders) > 0)

    def test_get_order_detail(self):
        # Test de récupération des détails d'une commande spécifique
        order_id = 1  # Remplacez par un ID valide existant dans votre système
        response = self.app.get(f'/orders/{order_id}')
        self.assertEqual(response.status_code, 200)
        order = json.loads(response.data)
        self.assertEqual(order['order_id'], order_id)

    def test_put_order(self):
        # Test de mise à jour d'une commande existante
        order_id = 1  # Remplacez par un ID valide existant dans votre système
        data = {
            'product': 'Updated Product',
            'quantity': 20
        }
        response = self.app.put(f'/orders/{order_id}', json=data)
        self.assertEqual(response.status_code, 200)
        updated_order = json.loads(response.data)
        self.assertEqual(updated_order['product'], 'Updated Product')
        self.assertEqual(updated_order['quantity'], 20)

    def test_delete_order(self):
        # Test de suppression d'une commande
        order_id = 1  # Remplacez par un ID valide existant dans votre système
        response = self.app.delete(f'/orders/{order_id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
