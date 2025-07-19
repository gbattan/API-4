# main.py

def display_products(products_data):
    products = products_data.get("products", [])
    if not products:
        return "No hay productos para mostrar."

    output = []
    for product in products:
        status = "En stock" if product["in_stock"] else "Sin stock"
        output.append(
            f"{product['id']}. {product['name']} - {product['description']}\n"
            f"   Precio: {product['price']} {product['currency']} | {status}"
        )
    return "\n".join(output)
