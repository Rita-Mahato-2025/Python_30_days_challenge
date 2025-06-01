#inventory system using nested dictionaries
inventory = {
    'Pen':{'quantity': 100, 'price': 35},
    'Notebook':{'quantity': 50, 'price': 75}
}

#function to add new product or update quantity
def add_product(pname, qty, price):
    if pname in inventory:
        inventory[pname]['quantity'] += qty
        print(pname, "updated new quantity:", inventory[pname]['quantity'])
    else:
        inventory[pname] = {'quantity': qty, 'price': price}
        print(pname, qty ,"added successfully")

#function to sell a product
def sell_product(pname, qty):
    if pname in inventory:
        if inventory[pname]['quantity'] >= qty:
            inventory[pname]['quantity'] -= qty
            print("Sold", qty, pname)
        else:
            print("Not enough", pname, "in stock")
    else:
        print(pname, "Not found in inventory.")

#Check availability
def check_inventory(pname):
    if pname in inventory:
        qty = inventory[pname]["quantity"]
        price = inventory[pname]["price"]
        print(pname, "Stock:", qty, "Price:",price)

#display inventory
def display_inventory():
    for pname in inventory:
        print(pname +" Quantity:", inventory[pname]["quantity"], "Price:", inventory[pname]["price"])

add_product("Pencil", 30, 3)
sell_product("Pen", 10)
check_inventory("Notebook")
display_inventory()