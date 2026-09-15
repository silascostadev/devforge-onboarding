def calculate_total(prices):
    subtotal_prices = 0.0
    for order in prices:
        subtotal_prices += order
    return subtotal_prices

def apply_discount(subtotal):
    subtotal_discount = 0.0
    if subtotal >= 60.0:
        return 0.15
    elif subtotal >= 40.0:
        return 0.10
    else:
        return 0.0

order = [15.0, 18.50, 32.0, 4.50]

subtotal = calculate_total(order)

discount_rate = apply_discount(subtotal)

final_amount = subtotal - (subtotal * discount_rate)

print(f"Subtotal: {subtotal:.2f}")
print(f"Desconto: {discount_rate * 100:.0f}%")
print(f"Valor Final: {final_amount:.2f}")