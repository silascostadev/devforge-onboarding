order_prices = [12.50, 8.00, 24.50, 15.00, 9,00]
is_takeaway = True
subtotal = 0.0

for prices in order_prices:
    subtotal += prices

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