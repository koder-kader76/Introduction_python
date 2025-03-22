# python

def calculate_total(cart):
    subtotal = 0
    for item in cart:
        name = item["name"]
        # print('name is', name)
        
        price = item["price"]
        # print('price is', price)
        
        quantity = item["quantity"]
        # print('quantity is', quantity)

        # bug is here; price * quantity
        # item_total = price + quantity
        
        # amended line
        item_total = price * quantity
        # print('item_total is', item_total)

        subtotal += item_total
        # print('subtotal is', subtotal)
        
        print(f"Added {quantity} {name}(s) at ${price} each")
    
    # Apply discount for purchases over $100
    if subtotal > 100:
        discount = subtotal * 0.025
        print(f"Discount applied: ${discount}")
        total = subtotal - discount
    else:
        total = subtotal
    
    return total

# Test shopping cart
shopping_cart = [
    {"name": "Laptop", "price": 800, "quantity": 1},
    {"name": "Mouse", "price": 25, "quantity": 2},
    {"name": "Notebook", "price": 5, "quantity": 3}
]

total_price = calculate_total(shopping_cart)
print(f"Total price: ${total_price}")


# Test shopping cart
shopping_cart2 = [
    {"name": "vase", "price": 20, "quantity": 1},
    {"name": "lamp", "price": 10, "quantity": 2},
    {"name": "pencil", "price": 1, "quantity": 100}
]

total_price2 = calculate_total(shopping_cart2)
print(f"Total price: ${total_price2}")