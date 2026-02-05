
# Restaurant POS & Billing System
# Author: Python Developer Intern (Unified Mentor)

GST_RATE = 0.05
SERVICE_CHARGE_RATE = 0.10

menu = {
    "Burger": {"price": 120, "stock": 50},
    "Pizza": {"price": 250, "stock": 30},
    "Pasta": {"price": 180, "stock": 40},
    "Cold Drink": {"price": 60, "stock": 100},
    "Ice Cream": {"price": 90, "stock": 60}
}

daily_sales = []
item_sales_count = {}

def display_menu():
    print("\n------ MENU ------")
    for item, details in menu.items():
        print(f"{item}: ₹{details['price']} | Stock: {details['stock']}")
    print("------------------")

def take_order():
    order = {}
    while True:
        display_menu()
        item = input("Enter item name (or 'done' to finish): ").strip().title()
        if item == "Done":
            break
        if item not in menu:
            print("Invalid item.")
            continue
        try:
            qty = int(input("Enter quantity: "))
            if qty <= 0:
                raise ValueError
        except ValueError:
            print("Invalid quantity.")
            continue
        if qty > menu[item]["stock"]:
            print("Insufficient stock.")
            continue
        order[item] = order.get(item, 0) + qty
    return order

def calculate_bill(order):
    subtotal = sum(menu[item]["price"] * qty for item, qty in order.items())
    gst = subtotal * GST_RATE
    service = subtotal * SERVICE_CHARGE_RATE
    total = subtotal + gst + service
    return subtotal, gst, service, total

def update_inventory(order):
    for item, qty in order.items():
        menu[item]["stock"] -= qty
        item_sales_count[item] = item_sales_count.get(item, 0) + qty

def print_bill(order, subtotal, gst, service, total):
    print("\n----- BILL -----")
    for item, qty in order.items():
        print(f"{item} x {qty} = ₹{menu[item]['price'] * qty}")
    print(f"Subtotal: ₹{subtotal}")
    print(f"GST: ₹{gst}")
    print(f"Service Charge: ₹{service}")
    print(f"Total: ₹{total}")
    print("----------------")

def daily_summary():
    print("\nDAILY SUMMARY")
    revenue = sum(s["total"] for s in daily_sales)
    print(f"Total Revenue: ₹{revenue}")
    if item_sales_count:
        top = max(item_sales_count, key=item_sales_count.get)
        print(f"Most Sold Item: {top}")
    else:
        print("No sales yet")

def cashier_menu():
    while True:
        print("\n1. Take Order\n2. Exit")
        choice = input("Choose: ")
        if choice == "1":
            order = take_order()
            if not order:
                print("No order placed.")
                continue
            subtotal, gst, service, total = calculate_bill(order)
            update_inventory(order)
            print_bill(order, subtotal, gst, service, total)
            daily_sales.append({"order": order, "total": total})
        elif choice == "2":
            break
        else:
            print("Invalid option")

def manager_menu():
    while True:
        print("\n1. View Menu\n2. Daily Summary\n3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            display_menu()
        elif choice == "2":
            daily_summary()
        elif choice == "3":
            break
        else:
            print("Invalid option")

def main():
    while True:
        print("\nLogin as:\n1. Cashier\n2. Manager\n3. Exit")
        role = input("Choose: ")
        if role == "1":
            cashier_menu()
        elif role == "2":
            manager_menu()
        elif role == "3":
            print("Goodbye")
            break
        else:
            print("Invalid role")

if __name__ == "__main__":
    main()
