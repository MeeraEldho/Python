print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10 12 15"))
people = int(input("How many people to spilt the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each perosn should pay: ${final_amount}")
