# create a dic with the prices
PIZZA_PRICES = {"S": 15, "M": 20, "L": 25}
PIZZA_NAME = {"S": "Cheap Ass Pizza", "M": "Not so Hungry Pizza", "L": "`Stop you fat fuck` Pizza"}
PEPPERONI_COST = {"S": 2, "M": 3, "L": 3}
EXTRA_CHEESE_COST = 1

def calculate_bill(size, add_pepperoni, add_extra_cheese):
    # Base price based on size
    if size not in PIZZA_PRICES:
        raise ValueError("Invalid pizza size selected.")
    bill = PIZZA_PRICES[size]

    # Add costs for extras
    if add_pepperoni == "Y":
        bill += PEPPERONI_COST[size]
    if add_extra_cheese == "Y":
        bill += EXTRA_CHEESE_COST

    return bill


print("Welcome to Python Pizza Deliveries!")
try:
    size = input("What size pizza do you want? S, M or L: ").upper()
    add_pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    add_extra_cheese = input("Do you want extra cheese? Y or N: ")

    total_bill = calculate_bill(size, add_pepperoni, add_extra_cheese)
    print(f"Your {PIZZA_NAME[size]} cost is: ${total_bill}.")
except ValueError as e:
    print(e)