def calculate_payment(total_bill, tip_percentage, num_people):
    total_with_tip = total_bill * (1 + tip_percentage)
    return round(total_with_tip / num_people, 2)


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10 12 15 ")) / 100
people = int(input("How many people to split the bill? "))

individual_payment = calculate_payment(bill, tip_percentage, people)
print(f"Each person should pay: ${individual_payment:.2f}")
