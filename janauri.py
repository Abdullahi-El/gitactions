janaury_bills = {"rent": 5515, "food": 2000, "bills": 2900, "family": 1600}

# Using the sum() function to calculate the total amount
total_amount = sum(janaury_bills.values())

Salary = 12000

# Calculate the remaining amount    
remaining_amount = Salary - total_amount

print(f"The remaining amount January has to pay is: {remaining_amount}")

# Check if any bill is greater than 2000
for value in janaury_bills.values():
    if value > 2000:
        print(f"'{value}' is too much")
    else:
        print(f"'{value}' is not too much")
