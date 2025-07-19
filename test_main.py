# test_main.py

import unittest
from main import display_products

class TestDisplayProducts(unittest.TestCase):

    def test_display_with_products(self):
        data = {
    "products": [
        {
            "id": 1,
            "name": "iPhone 13",
            "description": "The latest iPhone from Apple",
            "price": 999.99,
            "currency": "USD",
            "in_stock": False
        },
        {
            "id": 2,
            "name": "Samsung Galaxy S21",
            "description": "The latest Samsung phone",
            "price": 899.99,
            "currency": "USD",
            "in_stock": False
        },
        {
            "id": 3,
            "name": "Google Pixel 6",
            "description": "The latest Google phone",
            "price": 799.99,
            "currency": "USD",
            "in_stock": False
        },
        {
            "id": 4,
            "name": "Motorola Edge 30",
            "description": "Motorola's mid-range smartphone",
            "price": 599.99,
            "currency": "USD",
            "in_stock": False
        }
    ]
}
        output = display_products(data)
        print(output)
        self.assertIn("iPhone 13", output)
        self.assertIn("Precio: 999.99 USD", output)

    def test_display_with_empty_list(self):
        data = {"products": []}
        output = display_products(data)
         # Mensaje que se verá siempre en la consola
        print("Verificando comportamiento con lista de productos vacía...")
        print(f"Resultado obtenido: {output}")

    # Mensaje que se verá si la prueba falla
        self.assertEqual(
        output,
        "No hay productos para mostrar.",
        msg="FALLÓ: La función no devolvió el mensaje esperado para una lista vacía."
        )

if __name__ == '__main__':
    unittest.main()
