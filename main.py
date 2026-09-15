def calculate_total(prices):
    subtotal_calculated = 0.0
    for product in prices:
        subtotal_calculated += product["unit_price"] * product["quantity"]
    return subtotal_calculated
    

def apply_discount(subtotal):
    subtotal_discount = 0.0
    if subtotal >= 60.0:
        return 0.15
    elif subtotal >= 40.0:
        return 0.10
    else:
        return 0.0

order_items = [
    {"name": "Café Coado", "unit_price": 5.00, "quantity": 2},
    {"name": "Croissant", "unit_price": 11.50, "quantity": 2},
    {"name": "Brownie de Chocolate", "unit_price": 9.00, "quantity": 3},
]

print("Pedido:")

for item in order_items:
    print(f"Item: {item["name"]} X{item["quantity"]}")

subtotal = calculate_total(order_items)

discount_rate = apply_discount(subtotal)

final_amount = subtotal - (subtotal * discount_rate)

print(f"Subtotal: {subtotal:.2f}")
print(f"Desconto: {discount_rate * 100:.0f}%")
print(f"Valor Final: {final_amount:.2f}")