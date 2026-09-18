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

def register_item():
    try:
        name = str(input("Qual o nome do produto: "))
        unit_price = float(input("Qual o preço do produto: "))
        quantity = int(input("Qual a quantidade de produtos: "))

        order_items_func = {"name": name, "unit_price": unit_price, "quantity": quantity}
        
        return order_items_func
    except ValueError:
        print("Tipo de entrada inválida")
        return None

cart = []

while True:

    try:
        menu = int(input("1 - Adicionar Item / 2 - Fechar conta e sair: "))
        
    except ValueError:
        print("Entrada Inválida")   
        

    try:

        if menu == 1:
            new_item = register_item()
            if new_item is not None:
                cart.append(new_item)
            else:
                print("Produto não cadastrado. Erro na entrada")
        elif menu == 2:
            break
        else:
            print("Entrada inválida")

    except NameError:
        break

    
def calculos(carrinho):
    subtotal = calculate_total(cart)
    discount_rate = apply_discount(subtotal)
    final_amount = subtotal - (subtotal * discount_rate)

    print(f"Subtotal: {subtotal:.2f}")
    print(f"Desconto: {discount_rate * 100:.0f}%")
    print(f"Valor Final: {final_amount:.2f}")

for produtos in cart:
    print(f"Produto: {produtos['name']}/ Preço: {produtos['unit_price']} x{produtos['quantity']} = {produtos['unit_price'] * produtos['quantity']}")


if len(cart) == 0:
    print("Nenhum item foi registrado. Sistema finalizado")
else:
    calculos(cart)


