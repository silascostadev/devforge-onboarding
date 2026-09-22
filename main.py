import json

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

def save_order_to_json(carrinho, subtotal, discount, total):

    orders = {"items": carrinho, "subtotal": subtotal, "discount_rate": discount, "total_payable": total}
    with open("ultimo_pedido.json", "w", encoding="utf-8") as file:
        json.dump(orders, file, indent=4, ensure_ascii=False)
        print("[SUCESSO] Pedido salvo em 'ultimo_pedido.json!'")



def load_last_order():
    try:
        with open("ultimo_pedido.json", "r", encoding="utf-8") as file:
            last_order=json.load(file)
            for names in last_order['items']:
                print(f"Itens: {names['name']}, Valor: {names['unit_price']:.2f} x {names['quantity']} = {names['unit_price']*names['quantity']:.2f}")
            print(f"Subtotal: {last_order['subtotal']}")
            print(f"Taxa de Desconto: {last_order['discount_rate']*100:.0f}%")
            print(f"Total Pago: {last_order['total_payable']:.2f}")
    except FileNotFoundError:
        print("[AVISO] Arquivo não encontrado")


cart = []

while True:

    try:
        menu = int(input("1 - Adicionar Item / 2 - Ver ultimo pedido / 3 - Fechar conta e sair: "))
        
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
            load_last_order()

        elif menu == 3: 
            break
        else:
            print("Entrada inválida")

    except NameError:
        break

    

subtotal = calculate_total(cart)
discount_rate = apply_discount(subtotal)
final_amount = subtotal - (subtotal * discount_rate)





for produtos in cart:
    print(f"Produto: {produtos['name']}/ Preço: {produtos['unit_price']} x{produtos['quantity']} = {produtos['unit_price'] * produtos['quantity']}")

print(f"Subtotal: {subtotal:.2f}")
print(f"Desconto: {discount_rate * 100:.0f}%")
print(f"Valor Final: {final_amount:.2f}")

if len(cart) == 0:
    print("Nenhum item foi registrado. Sistema finalizado")
else:
    save_order_to_json(cart, subtotal, discount_rate, final_amount) 

 

