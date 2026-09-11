product_name = "Mocha Especial"
product_price = 14.50
items_sold = 3
is_takeaway = True
subtotal = product_price * items_sold

discount: 0.0

if subtotal >= 60.0:
    discount = 0.15
elif subtotal >= 40.0:
    discount = 0.10
else:
    discount = 0.0

saved_amount = subtotal * discount

final_price = subtotal - saved_amount

print(f"Subtotal: {subtotal:.2f}")
print(f"Desconto: {discount * 100:.0f}%")
print(f"Valor Final: {final_price:.2f}")